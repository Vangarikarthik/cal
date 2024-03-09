pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "my-flask-app:latest"
        
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_TAG .'
            }
        }
        
        stage('Deploy') {
            steps {
                sh "kubectl apply -f deploy.yaml"
                sh "kubectl apply -f service.yaml"
              
            }
        }
    }
}

