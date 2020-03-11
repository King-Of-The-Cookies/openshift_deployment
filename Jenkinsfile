
//def ref = "hi"

node() {
properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'reference', value: '$.ref', regexpFilter:'refs/heads/'],

    ],
    causeString: 'Triggered on',

    token: 'abc123',

    printContributedVariables: true,

    regexpFilterText: '$reference',
    regexpFilterExpression: 'test|master|develop'

   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell: $reference"
 }
}


















