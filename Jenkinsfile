pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/app.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -s app'
            }
        }
    }
}
