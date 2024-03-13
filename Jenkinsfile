pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "karthikvangari/my-flask-app:latest"
        CONTAINER_NAME="my-flask-container"
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_TAG .'
            }
        }
        
        stage('run') {
            steps {
                
                
                sh "docker stop $CONTAINER_NAME || true"
                sh "docker rm $CONTAINER_NAME || true"
                sh "docker run -d -t --name $CONTAINER_NAME -p 5001:5000 $IMAGE_TAG"
              
            }
        }
     stage('push') {

          steps {

               sh "docker login -u karthikvangari -p Karthik@9666 "
               sh "docker push $IMAGE_TAG" 
}
}
   stage('deploy') {
 
           steps {

              sh "kubectl apply -f "deploy.yaml""
              sh "kubectl apply -f "service.yaml""
              sh "minikube service my-first-app-service"

    }
}

}
}
