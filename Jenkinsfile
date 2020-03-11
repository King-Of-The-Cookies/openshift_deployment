
//def ref = "hi"

node() {

properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'reference', value: '$.ref'],

    ],
    causeString: 'Triggered on',

    token: 'abc123',

    printContributedVariables: true,

   ]
  ])
 ])


 stage("build") {

  sh "echo Variables from shell"
 }
}


























