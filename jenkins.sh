#!/bin/bash 

echo "Installing the parabank docker application"
docker pull parasoft/parabank
echo "Installing the python packages"
python3 -m pip install --break-system-packages -r requirements.txt
echo "Starting the parabank docker application"
docker run -d -p 8080:8080 -p 61616:61616 -p 9001:9001 parasoft/parabank
# Temporary workaround, sometimes the HYSQL wont start up no matter what..
echo "Waiting for the service startup (60 s)"
sleep 45
curl http://localhost:8080/parabank/index.htm > /dev/null
sleep 25
curl http://localhost:8080/parabank/admin.htm > /dev/null
sleep 15
echo "Starting the tests"
if [ -z $@ ]
  then
    BROWSER="chrome";
elif [ -n $@ ]
  then
    BROWSER=$1;
fi
python3 -m pytest --browser-name $BROWSER
echo "Generating the report"
allure serve allure-results
