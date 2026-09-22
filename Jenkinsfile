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

