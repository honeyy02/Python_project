pipeline {
    agent any
    environment {
        PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
    }
    stages {
        
        stage('Run tests with coverage') {
            steps {
                script {
                    // Run tests, capture the exit status, but don't stop the pipeline
                    def testStatus = sh(script: 'pytest --cov=app --cov-report=html test/', returnStatus: true)
                    // Generate the coverage report regardless of the test results

                    // If tests failed, generate a report for only failed tests
                    if (testStatus != 0) {
                        echo "Some Tests failed, but the artifacts will be synced."
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
    post {
        always {
            script {
                // def buildNumber = currentBuild.number
                // sh "mv htmlcov htmcov_${buildNumber}"
                archiveArtifacts artifacts: 'htmlcov/**', allowEmptyArchive: true
                echo "::: Pipeline executed successfully :::"
         }
    }
    success {
            script {
                // Set the build description with the build number on successful build
                currentBuild.description = "Last successful build number: ${currentBuild.number}"
            }
        }
}
}