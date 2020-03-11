

def now = new Date()
def timestamp = now.format("yyyyMMddHHmmssSSS")
def project = null
def buildProject = null

node() {

 stage("checkout") {

  sh "echo checking out scm"

  checkout scm
 }

 stage("test"){
 sh "source /var/lib/jenkins/shiningpanda/jobs/9dddd5ce/virtualenvs/d41d8cd9/bin/activate"
 sh "/var/lib/jenkins/shiningpanda/jobs/9dddd5ce/virtualenvs/d41d8cd9/bin/pip install -r requirements.txt"
 sh "/var/lib/jenkins/shiningpanda/jobs/9dddd5ce/virtualenvs/d41d8cd9/bin/python3 tests/test.py"

 }



 stage("analysis"){
 sh "echo placeholder for analysis"
 }


 if ((env.BRANCH_NAME=="master")||(env.BRANCH_NAME=="test")){
    if (env.BRANCH_NAME=="master"){
    project = "prod"
    buildProject = "prod-build"
    } else {
    project = "test"
    buildProject = "test-build"
    }

    //single credential needed: gittoken

    withCredentials([
    string(credentialsId: '32611c6e-b8f8-4b08-beeb-ef94aca8b00a', variable: 'token')
    ]){
    openshift.withCluster("https://192.168.99.100:8443", "NHypC6X6Xab1BkT8eHexaQ3KwjV0Yau57mRZrDbh9u4"){
        openshift.withProject(project){

       stage("apply build template in ${buildProject}"){

        sh "echo ${token}"

     }

     stage("start build"){


     }

     stage("deploy"){

     }

     stage("deployment testing"){
     sh "echo placeholder for deployment tests"

     }


    }


        }


    }
 }
}

