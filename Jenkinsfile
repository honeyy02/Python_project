pipeline{
    agent any
    stages{
        stage("Install dependecies"){
            steps{
                script{
                sh 'pip install pytest pytest-cov'
            }
            }
            
        }
        stage("Run the test cases with cov"){
            steps{
                script{
                    def testSt = sh(script : 'pytest --cov=app --cov-report=html test/', returnStatus: true)
                    if(testSt!=0){
                        echo"Test case are failed"
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
    post{
        always{
            echo "Pipeline SUCCESS"
            archiveArtifact artifacts:'htmlcov/**', allowEmptyArchive: true

        }
    }
}