pipeline {
    agent any
    stages{
        stage('Clone') {
            steps {
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/theanhgk16/Blog.git'
            }
        }
        stage('Push Docker Hub'){
            steps{
                // This step should not normally be used in your script. Consult the inline help for details.
                withDockerRegistry(credentialsId: 'dockerhub', url:'') {
                    // some block
                    sh label: '', script: 'docker build -t anhnt123/devops-anhnt:latest .'
                    sh label: '', script: 'docker push anhnt123/devops-anhnt:latest'
                }
            }
        }
    }
}