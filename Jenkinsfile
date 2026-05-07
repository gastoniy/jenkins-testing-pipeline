pipeline {
    agent {
        label 'docker-agent-with-python'
    }

    environment {
        IMAGE_NAME = "my-flask-app"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies'
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --no-cache-dir -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo 'Executing tests from test_app.py...'
                sh '''
                . venv/bin/activate
                pytest test_app.py --junitxml=test-results.xml
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building the Docker container...'
                sh 'docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .'
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded! The application is tested and the Docker image is built.'
        }
        failure {
            echo 'Pipeline failed! Check the Console Output for details.'
        }
    }
}
