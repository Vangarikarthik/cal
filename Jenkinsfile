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
                    retry(5) {
                        sh 'kubectl apply -f deploy.yaml'
                        sh 'kubectl apply -f service.yaml'
                        
                        def serviceStatus = sh(script: 'kubectl get svc my-first-app-service', returnStdout: true).trim()
                        if (serviceStatus.contains('pending')) {
                            echo 'Service is still pending. Retrying in 30 seconds...'
                            sleep 30
                            error 'Service not available yet'
                        }
                    }
                }
            }
        }
        
        stage('Open URL') {
            steps {
                script {
                    def serviceIP = sh(script: 'minikube service my-first-app-service --url', returnStdout: true).trim()
                    echo "Service URL: ${serviceIP}"
                    
                   sh 'firefox  ${serviceIP}"'
                }
            }
        }
    }
}
    


