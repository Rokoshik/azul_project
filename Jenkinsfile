pipeline {
    agent any

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
                script {
                    sh '''
                    # Unset any previous Python virtualenv environment variables
                    unset VIRTUAL_ENV
                    unset PYTHONPATH
                    unset PYTHONHOME

                    # Remove any existing venv in Jenkins workspace
                    rm -rf ./venv

                    # Clean PATH from any previous venvs, especially /home/kris/azul_project/venv/bin
                    export PATH=$(echo $PATH | tr ':' '\\n' | grep -v '/home/kris/azul_project/venv/bin' | paste -sd ':' -)

                    # Optional: Remove pip caches to avoid stale package info
                    rm -rf /var/lib/jenkins/.cache/pip /var/lib/jenkins/.cache/pipenv /var/lib/jenkins/.local/share/virtualenvs/*

                    # Create new virtual environment inside workspace
                    python3 -m venv ./venv

                    # Activate the new virtual environment
                    . ./venv/bin/activate

                    # Print info for debugging
                    echo "VIRTUAL_ENV=$VIRTUAL_ENV"
                    which python
                    which pip
                    echo "PATH=$PATH"

                    # Upgrade pip explicitly inside this virtualenv
                    ./venv/bin/pip install --upgrade pip
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh '''
                    . ./venv/bin/activate
                    # Run your test commands here, for example:
                    pytest
                    '''
                }
            }
        }

        // Add further stages like 'Run CLI Tool', 'Archive Report' as needed
    }

    post {
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed. Please check logs.'
        }
    }
}
