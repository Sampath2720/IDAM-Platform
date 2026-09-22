pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest -v
                '''
            }
        }

        stage('Docker Build') {
            steps {
                sh '''
                docker build -t idam-platform:v1 .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop idam-app || true
                docker rm idam-app || true

                docker run -d \
                  --name idam-app \
                  -p 7070:7070 \
                  idam-platform:v1
                '''
            }
        }
    }
}
