pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Build stage: checking Python files'
                bat 'python --version'
                bat 'python -m py_compile app.py tests\\test_app.py'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s tests -v'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully.'
        }
        failure {
            echo 'CI pipeline failed. Check the stage logs.'
        }
    }
}
