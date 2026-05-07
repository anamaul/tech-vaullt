pipeline {
    agent any

    environment {
        // Menggunakan variabel environment Jenkins
        DOCKER_HUB_USER = 'muhammadmaulana'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/anamaul/tech-vaullt.git'
            }
        }

        stage('Build & Push') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {
                    // Menggunakan 'bat' untuk Windows dan format %VARIABLE%
                    bat """
                        echo %DOCKER_PASS% | docker login -u %DOCKER_USER% --password-stdin

                        docker build -t %DOCKER_HUB_USER%/techvault-backend:latest ./backend
                        docker build -t %DOCKER_HUB_USER%/techvault-frontend:latest ./frontend

                        docker push %DOCKER_HUB_USER%/techvault-backend:latest
                        docker push %DOCKER_HUB_USER%/techvault-frontend:latest
                    """
                }
            }
        }

        stage('Deploy') {
            steps {
                withCredentials([file(credentialsId: 'kubeconfig-aks', variable: 'KUBECONFIG_FILE')]) {
                    bat """
                        @echo off
                        set KUBECONFIG=%KUBECONFIG_FILE%

                        kubectl apply -f k8s/backend-deployment.yaml
                        kubectl apply -f k8s/backend-service.yaml
                        kubectl apply -f k8s/frontend-deployment.yaml
                        kubectl apply -f k8s/frontend-service.yaml
                        kubectl apply -f k8s/ingress.yaml

                        kubectl rollout restart deployment/backend-deployment
                        kubectl rollout restart deployment/frontend-deployment
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline berhasil! Aplikasi sudah di-deploy ke AKS.'
        }
        failure {
            echo 'Pipeline gagal. Cek log untuk detail error.'
        }
    }
}