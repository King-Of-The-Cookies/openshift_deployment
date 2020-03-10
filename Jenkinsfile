
def var = " "

node {
 properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'ref', value: '$.ref', regexpFilter: "/refs/heads/", defaultValue: ""],
     [key: 'action', value:'$.action', defaultValue: ""],
    [key: 'head_ref', value:'$.head.ref', defaultValue: ""],
    [key: 'base_ref', value:'$.base.ref', defaultValue: ""]

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