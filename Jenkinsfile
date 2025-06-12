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

        stage('Run Process Reporter') {
            steps {
                sh '''
                    ./venv/bin/python azul/process_reporter.py --output-format csv --output my_report
                '''
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
                    ./venv/bin/python -m unittest discover -s tests -p '*_test.py' -v > tests/reports/tests_output.log || true
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'tests/reports/tests_output.log', allowEmptyArchive: true
                    // junit 'tests/reports/*.xml' // optional: enable if you generate XML test reports
                }
            }
        }
    }
}
