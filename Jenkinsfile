pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
    }

    options {
        skipDefaultCheckout(true) // prevents automatic Git checkout before cleanWs
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Repo') {
            steps {
                checkout scm
            }
        }

        stage('Create & Activate Python venv') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python -m unittest discover tests
                '''
            }
        }

        stage('Run CLI Tool') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    python cli.py --format json --output test_report
                '''
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'test_report.json', fingerprint: true
            }
        }
    }
}
