pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/<твой-логин>/<твой-репо>.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t myapp:latest .'
            }
        }
    }
}
