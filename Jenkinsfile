pipeline{

    agent {
        label 'lamp'
    }

    stages{
        stage ("Preparing the environment"){
            steps{
                sh 'python3 -m pip install -r requirements.txt'
                sh 'python3 -m pip list'
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