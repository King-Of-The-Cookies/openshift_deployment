
//def ref = "hi"

node() {

properties([
  parameters([
  string(defaultValue: '', name:'reference'),
  string(defaultValue: '', name:'action'),
  ]),


  pipelineTriggers([
   [$class: "GenericTrigger",
    genericVariables: [
     [key: "reference", value: '$.ref', regexpFilter: "refs/heads/", defaultValue: ''],
     [key: "action", value: '$.action', defaultValue:''],

    ],
    causeString: "Triggered on",

    token: "abc123",

    printContributedVariables: true,

    //regexpFilterExpression: "${env.BRANCH_NAME}",
    //regexpFilterText: "${reference}"

   ]
  ])
 ])


 stage("build") {

  sh "echo Variables from shell ${env.BRANCH_NAME} ${reference} ${action}"
 }
}
































