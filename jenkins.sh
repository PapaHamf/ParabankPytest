#!/bin/bash 

echo "Installing the parabank docker application"
docker pull parasoft/parabank
echo "Starting the parabank docker application"
docker run -d -p 8080:8080 -p 61616:61616 -p 9001:9001 parasoft/parabank
sleep 20
echo "Starting the tests"
python3 -m pytest
