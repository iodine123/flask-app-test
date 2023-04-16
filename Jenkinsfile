pipeline{
    agent any
    stages{
        stage("Pull Source Code"){
            steps{
                sh """ 
                    rm -rf flask-app-test
                    git clone https://github.com/iodine123/flask-app-test.git -b master
                    cd flask-app-test
                    ls
                    """
            }
        }

        stage("Unit Test"){
            steps{
                sh """
                    python3 -m unittest flask-app-test/unit_test/apitest.py
                    """
            }
        }

        stage("Build Image"){
            steps{
                sh """
                    docker build -t registry.heroku.com/flask-trial/web flask-app-test/.
                    """
            }
        }

        stage("Push Image"){
            steps{
                sh """
                    docker push registry.heroku.com/flask-trial/web
                    """
            }
        }

        stage("Deploy Container on Heroku"){
            steps{
                sh """
                    heroku container:release web --app flask-trial
                """
            }
        }
    }
    
}