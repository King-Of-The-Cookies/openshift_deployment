
def now = new Date()
def timestamp = now.format("yyyyMMddHHmmssSSS")
def project = null

node() {

 stage("checkout") {

  sh "echo checking out scm"

  checkout scm
 }

 stage("test"){
 sh "echo placeholder for tests"
 }

 stage("analysis"){
 sh "echo placeholder for analysis"
 }

 if ((env.BRANCH_NAME=="master")||(env.BRANCH_NAME=="test")){
    if (env.BRANCH_NAME=="master"){
    project = "prod"
    } else {
    project = "test"
    }

    openshift.withCluster("https://192.168.99.100:8443", "NHypC6X6Xab1BkT8eHexaQ3KwjV0Yau57mRZrDbh9u4"){
        openshift.withProject(project){

        }


    }


 stage("apply build template"){


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

