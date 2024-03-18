pipeline {
    agent any
    
    environment {
        IMAGE_TAG = "karthikvangari/my-flask-app:latest"
        CONTAINER_NAME="my-flask-container"
        KUBECONFIG = '/var/lib/jenkins/.kube/config'
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
        
       stage('push'){
              
           steps {

            sh "docker login -u karthikvangari -p Karthik@9666"
            sh "docker push  $IMAGE_TAG"
}

    }
     
            stage('Deploy') {
            steps {
                script {
                    retryCount = 0
                    maxRetries = 5
                    serviceAvailable = false
                    
                    sh 'minikube start'
                    sh 'kubectl apply -f "deploy.yaml"'
                    sh 'kubectl apply -f "service.yaml"'
                    export BROWSER=/usr/bin/firefox
                          
                    
                    while (!serviceAvailable && retryCount < maxRetries) {
                        try {
                            sh 'minikube service my-first-app-service'
                            serviceAvailable = true
                        } catch (Exception e) {
                            echo "Service not available. Retrying..."
                            retryCount++
                            sleep 30 // Adjust the sleep time as needed
                        }
                    }

                    if (!serviceAvailable) {
                        error('Failed to deploy service after multiple retries')
                    }
                }
            }
        }
    }
}

