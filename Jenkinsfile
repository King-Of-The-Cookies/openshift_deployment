
//def ref = "hi"

node() {

properties([
  pipelineTriggers([
   [$class: "GenericTrigger",
    genericVariables: [
     [key: "reference", value: '$.ref', regexpFilter: "refs/heads/"],

    ],
    causeString: "Triggered on",

    token: "abc123",

    printContributedVariables: true,

    regexpFilterExpression: "master|test|develop",
    regexpFilterText: '$reference'

   ]
  ])
 ])


 stage("build") {

  sh "echo Variables from shell ${env.BRANCH_NAME}"
 }
}




























