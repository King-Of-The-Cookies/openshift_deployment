
def now = new Date()
def timestamp = now.format("yyyyMMddHHmmssSSS")

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

 if ((env.BRANCH_NAME=="master")||(env.BRANCH_NAME=="develop")){

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

