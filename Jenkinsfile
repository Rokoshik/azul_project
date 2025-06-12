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
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Assuming you have automated tests in tests/ directory
                sh '''
                    mkdir -p tests/reports
                    ./venv/bin/python -m unittest discover -s tests -p '*_test.py' -v > tests/reports/tests_output.log || true
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'tests/reports/tests_output.log', allowEmptyArchive: true
                    // Uncomment and adjust if you generate JUnit XML reports
                    // junit 'tests/reports/*.xml'
                }
            }
        }
    }
}
