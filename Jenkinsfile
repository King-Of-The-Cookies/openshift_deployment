
//def ref = "hi"

node() {
properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'reference', value: '$.ref', regexpFilter:'refs/heads/'],
     [key: 'actions', value: '$.action'],

    ],
    causeString: 'Triggered on',

    token: 'abc123',

    printContributedVariables: true,

    regexpFilterText: '$reference $actions',
    regexpFilterExpression: 'test opened|master opened|develop opened'

   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell"
 }
}




















