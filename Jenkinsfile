pipeline {
    agent {
        dockerfile { 
            filename 'Dockerfile'
            args '-u root:sudo'
        }
    }
    stages {
        stage('Build and install dependecies') {
            steps {
                script {
                    sh """
                        python -m pip install --upgrade pip &&
                        pip install pytest
                    """
                }
            }
        }
        stage('Test with pytest') {
            steps {
                script {
                    sh """
                        pytest
                    """
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Jestem w sekcji deploymentu'
            }   
        }
    }
}
