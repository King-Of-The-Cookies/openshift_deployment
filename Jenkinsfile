

node(){

properties([
[$class: 'GenericTrigger',
genericHeaderVariables: [
    [key: 'X-GitHub-Event']
],
genericVariables: [
    [key: 'ref', value:'$.ref'],

    [key: 'action', value:'$.action'],
    [key: 'head_ref', value:'$.head.ref'],
    [key: 'base_ref', value:'$.ref']
],
causeString: 'Triggered by ${X-GitHub-Event}'


]])

    stage("test1"){
    sh "echo ${X-GitHub-Event}"
    }

}







