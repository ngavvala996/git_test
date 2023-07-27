pipeline {
    agent any

    stages {
        stage('Build and Test') {
            steps {
                // Build the Docker image
                sh 'docker build -t my-python-app .'
                
                // Run the Docker container and execute the pytest command
                sh 'docker run --rm -v $PWD:/app my-python-app pytest'
            }
        }
    }
}
