

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


 if ((env.BRANCH_NAME=="master")||(env.BRANCH_NAME=="test")||(hoi == true){
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
    openshift.withCluster(){
        openshift.withProject(project){
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
}

