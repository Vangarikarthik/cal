pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "my-flask-app:latest"
        CONTAINER_NAME = "my-flask-container"
        NGROK_AUTH_TOKEN = credentials('ngrok-auth-token') // Assuming you have Jenkins credentials configured for Ngrok Auth Token
        NGROK_BINARY_PATH = "/usr/local/bin/ngrok" // Update this path with the correct path to the ngrok binary
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
                sh "$NGROK_BINARY_PATH authtoken $NGROK_AUTH_TOKEN"
                sh "$NGROK_BINARY_PATH http 5001"
            }
        }
    }
}

