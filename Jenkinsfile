
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

    regexpFilterText: "$head_ref",
    regexpFilterExpression: "master|test"

   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell:"
 }
}