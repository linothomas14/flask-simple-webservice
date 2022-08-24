pipeline {
    environment {
    DOCKERHUB_CREDENTIALS = credentials('docker_hub_linothomas')
    }
    agent any 
    stages { 
        stage('Clone repo') {
            steps{
                git branch: 'main', credentialsId: 'github-linothomas14', url: 'https://github.com/linothomas14/flask-simple-webservice'
            }
        }
        stage('login to dockerhub') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('Build docker image') {
            steps {  
                sh 'sudo docker build -t linothomas/flask-simple-webservice:latest .'
            }
        }
        stage('Push to DockerHub'){
            steps {
                sh 'sudo docker push linothomas/flask-simple-webservice:latest'
            }
        }
        stage('Run Images'){
            steps {
                sh 'sudo docker rm -f $(docker ps -a -q) || true && sudo docker pull linothomas/flask-simple-webservice:latest && sudo docker run -d -p 80:5000 --name flask-simple-webservice linothomas/flask-simple-webservice:latest'
            }
        }
}
}