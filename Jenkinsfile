pipeline {
    agent {
        docker {
            image 'docker:20.10.7'
            args '-v /var/run/docker.sock:/var/run/docker.sock -v /tmp:/tmp'
        }
    }
    environment {
        DOCKER_CONFIG = '/tmp'
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/krahyor/jenkinsdemo.git'
            }
        }
        stage('Build Image') {
            steps {
                sh 'docker build -t jenkins-demo-app:latest .'
            }
        }
        stage('Run Container') {
            steps {
                sh '''
                docker rm -f demo-app || true
                docker run -d -p 8081:8081 --name demo-app jenkins-demo-app:latest
                '''
            }
        }
    }
}
