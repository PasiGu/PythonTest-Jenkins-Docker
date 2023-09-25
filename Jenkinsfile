pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'python3 hello_world.py'
            }
        }
        stage('Testing file') {
            steps {
                sh "python3 -m pytest"
            }
        }
        stage('Deliver') {
            steps {
                echo "Deliver...."
            }
        } 
    }
}