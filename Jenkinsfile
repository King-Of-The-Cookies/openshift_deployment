
//def ref = "hi"

node() {

properties([
  parameters([
  string(defaultValue: 'none', name:'reference'),
  string(defaultValue: 'none', name:'action'),
  ]),


  pipelineTriggers([
   [$class: "GenericTrigger",
    genericVariables: [
     [key: "reference", value: '$.ref', regexpFilter: "refs/heads/"],
     [key: "action", value: '$.action', defaultValue:'none'],

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

  sh "echo Variables from shell ${env.BRANCH_NAME} ${reference} ${action}"
 }
}































