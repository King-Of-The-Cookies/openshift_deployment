
def var = " "

node {
 properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'ref', value: '$.ref', regexpFilter: "/refs/heads/", defaultValue: "none"],
     [key: 'action', value:'$.action', defaultValue: "none"],
    [key: 'head_ref', value:'$.head.ref', defaultValue: "none"],
    [key: 'base_ref', value:'$.base.ref', defaultValue: "none"]

    ],
    causeString: 'Triggered on $ref',

    token: 'abc123',

    printContributedVariables: true,

    regexpFilterText: "$ref/$action/$base_ref",
    regexpFilterExpression: "master//|test//|pull_request//opened/master|pull_request//opened/test"

   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell:"
 }
}