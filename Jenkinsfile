pipeline {
    agent any

	stages {
	    stage("Docker pull") {
	        steps {
	            echo "Installing the parabank docker application"
	            docker pull parasoft/parabank
	        }
	    }
	    stage("Python packages") {
	        steps {
	            echo "Installing the python packages"
                    python3 -m pip install --break-system-packages -r requirements.txt
	        }
	    }
	    stage("Starting app") {
	        steps {
	            echo "Starting the parabank docker application"
                    docker run -d -p 8080:8080 -p 61616:61616 -p 9001:9001 parasoft/parabank
	        }
	    }
	    stage("Wait for the service") {
	        steps {
	            # Temporary workaround, sometimes the HYSQL wont start up no matter what..
                    echo "Waiting for the service startup (30 s)"
                    sleep 30
                    curl http://localhost:8080/parabank/index.htm
                    sleep 15
                    curl http://localhost:8080/parabank/admin.htm
                    sleep 15
	        }
	    }
	    stage("Run tests")
	        steps {
	            python3 -m pytest
	        }
	}
}
