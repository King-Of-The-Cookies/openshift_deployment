
def var = " "

node {
 properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'ref', value: '$.ref', regexpFilter: "/refs/heads/"],
     [key: 'action', value:'$.action'],
    [key: 'head_ref', value:'$.head.ref'],
    [key: 'base_ref', value:'$.base.ref']

    ],
    genericHeaderVariables: [
     [key: 'x-github-event']
    ],

    causeString: 'Triggered on $ref',

    token: 'abc123',

    printContributedVariables: true,

    regexpFilterText: "$x_github_event/$ref/$action/$base_ref",
    regexpFilterExpression: "push/master//|push/test//|pull_request//opened/master|pull_request//opened/test"

   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell:" + x_github_event
 }
}