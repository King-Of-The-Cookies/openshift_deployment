

def now = new Date()
def timestamp = now.format("yyyyMMddHHmmssSSS")
def project = null
def buildProject = null
def hoi = true

node() {

 stage("checkout") {

  sh "echo checking out scm"

  checkout scm
 }

 stage("test"){

 }



 stage("analysis"){
 sh "echo placeholder for analysis"
 }


 if ((env.BRANCH_NAME=="master")||(env.BRANCH_NAME=="test")||(hoi == true)){
    if (env.BRANCH_NAME=="master"){
    project = "prod"
    buildProject = "prod-build"
    } else {
    project = "test"
    buildProject = "test-build"
    }

    //single credential needed: gittoken


    openshift.withCluster(){
        openshift.withProject("cicd"){
       stage("backup existing build"){

       }

       stage("apply build template in ${buildProject}"){

        def yaml = readYaml file: "build.yaml"
        def bc = openshift.process(yaml)
        openshift.apply(bc)
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
