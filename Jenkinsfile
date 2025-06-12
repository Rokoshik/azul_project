pipeline {
    agent any

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
                sh '''
                    rm -rf venv
                    python3 -m venv venv
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    ./venv/bin/pip install --upgrade pip
                    ./venv/bin/pip install -r requirements.txt
                    ./venv/bin/pip install flake8 pytest
                '''
            }
        }

        stage('Lint') {
            steps {
                sh './venv/bin/flake8 azul/'
            }
        }

        stage('Run Process Reporter') {
            steps {
                sh './venv/bin/python azul/process_reporter.py --output-format csv --output my_report.csv'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'my_report.csv', allowEmptyArchive: true
                }
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    mkdir -p tests/reports
                    ./venv/bin/pytest tests/ --junitxml=tests/reports/results.xml || true
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'tests/reports/results.xml', allowEmptyArchive: true
                    junit 'tests/reports/results.xml'
                }
            }
        }
    }
}
