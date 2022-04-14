pipeline{

    agent {
        label 'lamp'
    }

    stages{
        stage ("Code Quality"){
            steps{
                sh 'echo checking code quality'
            }      
        }
        stage ("Unit Tests"){
            steps{
                sh 'echo Testing the applications'
            }      
        }
        stage ("Build"){
            steps{
                sh 'echo Creating Application Package'
            }      
        }
        stage ("Delivery"){
            steps{
                sh 'echo Uploading Artifacts to repository'
            }      
        }
        stage ("Code Deploy"){
            steps{
                sh 'echo Deploying the applications'
            }      
        }
    }
}