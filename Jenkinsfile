pipeline {
    agent any

    environment {
        VENV_DIR = "${env.WORKSPACE}/venv"
    }

    stages {
        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Repo') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/Rokoshik/azul_project.git',
                        credentialsId: 'github-private-key'
                    ]]
                ])
            }
        }

        stage('Create & Activate Python venv') {
            steps {
                script {
                    sh '''
                        # Remove old virtualenv env vars and old venv from PATH
                        unset VIRTUAL_ENV
                        unset PYTHONHOME
                        export PATH=$(echo $PATH | tr ':' '\\n' | grep -v 'home/kris/azul_project/venv/bin' | paste -sd ':' -)

                        # Create new virtual environment inside Jenkins workspace
                        python3 -m venv "${VENV_DIR}"

                        # Activate venv and upgrade pip, then install requirements
                        . "${VENV_DIR}/bin/activate"

                        "${VENV_DIR}/bin/pip" install --upgrade pip

                        # Install dependencies (make sure requirements.txt exists in repo root)
                        "${VENV_DIR}/bin/pip" install -r requirements.txt
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                        . "${VENV_DIR}/bin/activate"
                        # Replace this with your actual test command
                        pytest tests/
                    '''
                }
            }
        }

        stage('Run CLI Tool') {
            steps {
                script {
                    sh '''
                        . "${VENV_DIR}/bin/activate"
                        # Replace with your CLI command, e.g.:
                        python cli_tool.py
                    '''
                }
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: '**/test-report.xml', allowEmptyArchive: true
            }
        }
    }

    post {
        failure {
            echo 'Build failed. Check the logs above for details.'
        }
    }
}
