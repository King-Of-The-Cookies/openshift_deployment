
//def ref = "hi"

node() {

properties([
  pipelineTriggers([
   [$class: "GenericTrigger",
    genericVariables: [
     [key: "reference", value: '$.ref', regexpFilter: "refs/heads/"],

    ],
    genericHeaderVariables: [
     [key: 'x_github_event'],
    ],
    causeString: "Triggered on",

    token: "abc123",

    printContributedVariables: true,

    regexpFilterExpression: "${env.BRANCH_NAME} push",
    regexpFilterText: '$reference $x_github_event'

   ]
  ])
 ])


 stage("build") {

  sh "echo Variables from shell ${env.BRANCH_NAME} $x_github_event"
 }
}






























