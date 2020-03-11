
//def ref = "hi"

node() {

properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'reference', value: '$.ref', regexpFilter: 'refs/heads/'],

    ],
    causeString: 'Triggered on',

    token: 'abc123',

    printContributedVariables: true,

    regexpFilterText: 'master|test|develop',
    regexpFilterExpression: '$reference'

   ]
  ])
 ])


 stage("build") {

  sh "echo Variables from shell"
 }
}



























