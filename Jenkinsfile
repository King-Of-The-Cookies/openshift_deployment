
//def ref = "hi"

node() {

properties([
  parameters([
  string(defaultValue: 'test', name:'testie')
  ])


  pipelineTriggers([
   [$class: "GenericTrigger",
    genericVariables: [
     [key: "reference", value: '$.ref', regexpFilter: "refs/heads/"],
     //[key: "action", value: '$.action', regexpFilter: ""],

    ],
    genericHeaderVariables: [
     [key: 'x_github_event', regexpFilter: ''],
    ],
    causeString: "Triggered on",

    token: "abc123",

    printContributedVariables: true,

    regexpFilterExpression: "${env.BRANCH_NAME}",
    regexpFilterText: "${reference}"

   ]
  ])
 ])


 stage("build") {

  sh "echo Variables from shell ${env.BRANCH_NAME} ${env.testie}"
 }
}































