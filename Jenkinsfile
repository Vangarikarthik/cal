pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "my-flask-app:latest"
        CONTAINER_NAME = "my-flask-container"
        NGROK_AUTH_TOKEN = credentials('ngrok-auth-token') // Assuming you have Jenkins credentials configured for Ngrok Auth Token
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_TAG .'
            }
        }
        
        stage('Deploy') {
            steps {
                sh "docker stop $CONTAINER_NAME || true"
                sh "docker rm $CONTAINER_NAME || true"
                sh "docker run -d --name $CONTAINER_NAME -p 5001:5000 $IMAGE_TAG"
                
                // Start Ngrok tunnel
                sh "./ngrok authtoken $NGROK_AUTH_TOKEN"
                sh "./ngrok http 5001"
            }
        }
    }
}

