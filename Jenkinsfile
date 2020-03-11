
//def ref = "hi"

node() {
 properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'ref', value: '$.ref'],

    ],
    causeString: 'Triggered on $ref',

    token: 'abc123',

    printContributedVariables: true,



   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell: ${ref}"
 }
}

