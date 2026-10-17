pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Laura'
        STUDENT_SURNAME = 'Tileugabyl'
        STUDENT_GROUP = 'IT2-2311'
        STUDENT_ID = '41586'
    }

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
                sh 'python3 -m unittest discover -s app -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t tileugabyl-laura-devops .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f tileugabyl-laura-jenkins 2>/dev/null || true

                    docker run -d \
                      --name tileugabyl-laura-jenkins \
                      -e STUDENT_NAME="$STUDENT_NAME" \
                      -e STUDENT_SURNAME="$STUDENT_SURNAME" \
                      -e STUDENT_GROUP="$STUDENT_GROUP" \
                      -e STUDENT_ID="$STUDENT_ID" \
                      tileugabyl-laura-devops

                    sleep 3
                    docker ps -a --filter name=tileugabyl-laura-jenkins
                    docker logs tileugabyl-laura-jenkins
                    docker inspect -f '{{.State.Running}}' tileugabyl-laura-jenkins | grep -q true
                '''
            }
        }
    }

    post {
        success {
            echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
            echo "Group: ${STUDENT_GROUP}"
            echo "Student ID: ${STUDENT_ID}"
            echo 'Pipeline completed successfully!'
        }
    }
}
