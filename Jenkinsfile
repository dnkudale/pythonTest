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
        stage ("Code Quality"){
            steps{
                sh 'python3 -m pylint app.py'
            }      
        }
        stage ("Tests"){
            steps{
                sh 'python -m pytest'
            }      
        }
        stage ("build"){
            steps{
                sh 'docker build https://github.com/dnkudale/pythonTest.git -t pythonTestApp:latest'
            }      
        }
        stage ("Deploy"){
            steps{
                sh 'docker run -itd -p 5000:5000 pythonTestApp:latest'
            }      
        }
    }
}