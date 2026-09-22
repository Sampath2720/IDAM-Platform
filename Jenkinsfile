pipeline {
    agent any

    environment {
        IMAGE_NAME = "idam-platform"
        IMAGE_TAG = "v1"
    }

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
                docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                set -e

                echo "Saving Docker image..."
                docker save ${IMAGE_NAME}:${IMAGE_TAG} -o ${IMAGE_NAME}.tar

                echo "Importing image into K3s..."
                timeout 300 sudo k3s ctr images import ${IMAGE_NAME}.tar

                echo "Restarting deployment..."
                kubectl rollout restart deployment/idam-platform

                echo "Waiting for rollout..."
                kubectl rollout status deployment/idam-platform --timeout=300s

                echo "Deployment completed successfully"
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check console logs.'
        }
    }
}
