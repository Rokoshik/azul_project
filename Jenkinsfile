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
                        unset VIRTUAL_ENV
                        unset PYTHONHOME
                        unset PYTHONPATH
                        export PATH=$(echo $PATH | tr ':' '\\n' | grep -v '/home/kris/azul_project/venv/bin' | paste -sd ':' -)
                        rm -rf ~/.cache/pip ~/.cache/pipenv ~/.local/share/virtualenvs/*

                        python3 -m venv "${VENV_DIR}"

                        . "${VENV_DIR}/bin/activate"

                        "${VENV_DIR}/bin/pip" install --upgrade pip
                        "${VENV_DIR}/bin/pip" install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh '''
                    . "${VENV_DIR}/bin/activate"
                    pytest tests/
                '''
            }
        }
        stage('Run CLI Tool') {
            steps {
                sh '''
                    . "${VENV_DIR}/bin/activate"
                    python cli_tool.py
                '''
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
