#!/bin/bash 

echo "Installing the parabank docker application"
docker pull parasoft/parabank
echo "Installing the python packages"
python3 -m pip install --break-system-packages -r requirements.txt
echo "Starting the parabank docker application"
docker run -d -p 8080:8080 -p 61616:61616 -p 9001:9001 parasoft/parabank
echo "Waiting for the service startup (3 min)"
sleep 3m
echo "Starting the tests"
python3 -m pytest
