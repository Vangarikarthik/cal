pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "my-flask-app:latest"
        CONTAINER_NAME = "my-flask-container"
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Vangarikarthik/cal.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_TAG .'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'docker run --rm $IMAGE_TAG python -m unittest discover tests'
            }
        }
        
        stage('Deploy') {
            steps {
                sh "docker stop $CONTAINER_NAME || true"
                sh "docker rm $CONTAINER_NAME || true"
                sh "docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_TAG"
            }
        }
    }
    
    post {
        always {
            // Cleanup
            sh "docker stop $CONTAINER_NAME || true"
            sh "docker rm $CONTAINER_NAME || true"
        }
    }
}

