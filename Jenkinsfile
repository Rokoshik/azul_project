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
                    # Clean any existing venv
                    rm -rf ./venv

                    # Unset env vars that might interfere
                    unset VIRTUAL_ENV
                    unset PYTHONPATH
                    unset PYTHONHOME

                    # Create a fresh virtual environment
                    python3 -m venv ./venv

                    # Activate the virtual environment
                    . ./venv/bin/activate

                    # Upgrade pip to latest
                    ./venv/bin/pip install --upgrade pip

                    # Install dependencies if requirements.txt exists
                    if [ -f requirements.txt ]; then
                      ./venv/bin/pip install -r requirements.txt
                    fi

                    # Ensure pytest is installed
                    ./venv/bin/pip install pytest
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    # Activate venv and run pytest
                    . ./venv/bin/activate
                    pytest
                    '''
                }
            }
        }

        // Optional: archive test reports, add other stages here
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
