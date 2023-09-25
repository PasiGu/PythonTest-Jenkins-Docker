pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                sh 'python3 new_program.py'
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
