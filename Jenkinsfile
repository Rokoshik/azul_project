pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Create & Activate Python venv') {
            steps {
                script {
                    sh '''
                    set -e
                    rm -rf ./venv
                    unset VIRTUAL_ENV PYTHONPATH PYTHONHOME
                    python3 -m venv ./venv
                    ./venv/bin/pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                      ./venv/bin/pip install -r requirements.txt
                    fi
                    ./venv/bin/pip install pytest
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    set -e
                    ./venv/bin/pytest --junitxml=report.xml
                    '''
                }
            }
        }

        stage('Archive Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        failure {
            echo 'Build failed. Check the logs above.'
        }
        success {
            echo 'Build succeeded!'
        }
    }
}
