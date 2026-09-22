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

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                docker save idam-platform:v1 -o idam-platform.tar

                sudo k3s ctr images import idam-platform.tar

                kubectl rollout restart deployment/idam-platform

                kubectl rollout status deployment/idam-platform
                '''
            }
        }
    }
}
