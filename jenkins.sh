#!/bin/bash 

echo "Installing the parabank docker application"
docker pull parasoft/parabank
echo "Installing the python packages"
python3 -m pip install --break-system-packages -r requirements.txt
echo "Starting the parabank docker application"
docker run -d -p 8080:8080 -p 61616:61616 -p 9001:9001 parasoft/parabank
# Temporary workaround, sometimes the HYSQL wont start up no matter what..
echo "Waiting for the service startup (30 s)"
sleep 30
curl http://localhost:8080/parabank/index.htm
sleep 15
curl http://localhost:8080/parabank/admin.htm
sleep 15
python3 -m pytest
