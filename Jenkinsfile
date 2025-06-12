pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        PYTHON = "${env.WORKSPACE}/${VENV_DIR}/bin/python"
        PIP = "${env.WORKSPACE}/${VENV_DIR}/bin/pip"
        PYTEST = "${env.WORKSPACE}/${VENV_DIR}/bin/pytest"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }
        
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh 'python3 -m venv venv'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh '''
                        ${PIP} install --upgrade pip
                        ${PIP} install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                dir("${env.WORKSPACE}") {
                    sh '''
                        ${PYTEST} -v azul_project/tests --junitxml=report.xml
                    '''
                }
            }
        }
    }

    post {
        always {
            junit 'report.xml'
        }
        failure {
            echo 'Build failed. Check the logs above.'
        }
        cleanup {
            cleanWs()
        }
    }
}
