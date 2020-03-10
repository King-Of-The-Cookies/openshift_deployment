

node {
 properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'ref', value: '$.ref'],
     [key: 'action', value:'$.action'],
    [key: 'head_ref', value:'$.head.ref'],
    [key: 'base_ref', value:'$.base.ref']

    ],
    genericHeaderVariables: [
     [key: 'X-GitHub-Event']
    ],

    causeString: 'Triggered on $ref',

    token: 'abc123',

    printContributedVariables: true,
    printPostContent: true,

    silentResponse: false,

   ]
  ])
 ])

 stage("build") {
  sh "echo Variables from shell:"
 }
}