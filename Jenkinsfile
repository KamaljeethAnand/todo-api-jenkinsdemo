pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/KamaljeethAnand/todo-api-jenkinsdemo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python test_app.py'
            }
        }
    }
}
