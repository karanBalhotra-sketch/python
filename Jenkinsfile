pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                // Checkout the code from the GitHub repository
                git url: 'https://github.com/karanBalhotra-sketch/python.git'
            }
        }
        
        stage('Build Server and Client') {
            steps {
                script {
                    // Navigate to server directory and build server
                    dir('server') {
                        sh 'python setup.py build'
                    }
                    // Navigate to client directory and build client
                    dir('client') {
                        sh 'python setup.py build'
                    }
                }
            }
        }
        
        stage('Run Unit Tests') {
            steps {
                script {
                    // Run tests on the server-side code
                    dir('tests') {
                        sh 'pytest server_tests.py'
                    }
                    // Run tests on the client-side code
                    dir('tests') {
                        sh 'pytest client_tests.py'
                    }
                }
            }
        }
        
        stage('Deploy to Test Environment') {
            steps {
                script {
                    // Navigate to server directory and run the server
                    dir('server') {
                        sh 'nohup python server.py &'
                    }
                    // Run a test client to verify communication
                    dir('client') {
                        sh 'python client.py'
                    }
                }
            }
        }
        
        stage('Code Quality Analysis') {
            steps {
                // Optional: Integrate tools like SonarQube for code quality analysis
                script {
                    sh 'sonar-scanner'
                }
            }
        }
        
        stage('Release to Production') {
            steps {
                // Assuming we have a production server or containerized environment
                echo 'Deploying to production environment...'
                // Add your deployment script/commands here
            }
        }
    }
    
    post {
        always {
            // Clean up
            echo 'Cleaning up...'
            sh 'pkill -f server.py'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
