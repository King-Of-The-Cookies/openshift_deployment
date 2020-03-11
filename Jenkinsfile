
def now = new Date()
def timestamp = now.format("yyyyMMddHHmmss.SSS")

node() {

 stage("checkout") {

  sh "echo checking out scm"

  checkout scm

  sh "echo ${timestamp}"
 }
}

