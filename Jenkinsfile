
//def ref = "hi"

node() {
 properties([
  pipelineTriggers([
   [$class: 'GenericTrigger',
    genericVariables: [
     [key: 'ref', value: '$.ref', regexpFilter: "/refs/heads/", defaultValue: "none"],

    ],
    causeString: 'Triggered on $ref',

    token: 'abc123',

    printContributedVariables: true,

    regexpFilterText: "$ref",
    regexpFilterExpression: "master|test"

   ]
  ])
 ])

 stage("build") {

  sh "echo Variables from shell: " + ref
 }
}

