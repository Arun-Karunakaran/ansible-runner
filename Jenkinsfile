//Declarative//
pipeline{
    options {
        buildDiscarder(logRotator(numToKeepStr: '15'))
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
    }
    agent { 
        label 'ansible-server' 
    }
    parameters {
        string(name: 'AWX_ROOT_DIR', 
        defaultValue: '/var/lib/awx', 
        description: 'AWX root directory')
        string(name: 'ANSIBLE_PROJ_ROOT_DIR', 
        defaultValue: '/var/lib/awx/projects/oreacl/', 
        description: 'Ansible project directory')
        string(name: 'ANSIBLE_PROJ_LOG_DIR', 
        defaultValue: '/var/lib/awx/projects/oreacl/logs', 
        description: 'Ansible project logs directory')
        string(name: 'lastFile',
        description: 'Last file in the log')
        string(name: 'custombuildName',
        description: 'custom build name')        
        choice choices: ['OR', 'LNR'], description: 'product name', name: 'product'
        choice choices: ['11.2.0', '11.4.0', '11.3.0'], description: 'version no', name: 'version'
        choice choices: ['a64.win', 'int.w32', 'a64.lnx'], description: 'platform ', name: 'os'
        choice choices: ['sanet', 'sanetruntime', 'nonet', 'ingresinstall'], description: 'select the installer type/ feature or component that you want to install  ', name: 'feature'
        choice choices: ['install_latestpatch', 'install_previouspatch', 'upgrade_tolatestpatch', 'upgrade_alltolatestpatch'], description: 'conditions to verify the install and upgrades for OR and LNR sanet, sanetruntime and nonet 64bit and 32bit patches', name: 'condition'
        string(name: 'limittohost',
        defaultValue: 'usau-or-dlw10',
        description: 'host name') 
    }
   stages{
        stage('codesync'){
            environment {
                BITBUCKET_COMMON_CREDS = credentials('ansible')
            }
            steps{
                dir("${env.AWX_ROOT_DIR}"){
                sh('''
                    cp ${env.ANSIBLE_PROJ_ROOT_DIR}/setup.yml ${env.AWX_ROOT_DIR}
                    ansible-playbook --vault-password-file ~/.vault_pass setup.yml -e "ansible_become_password=$BITBUCKET_COMMON_CREDS_PSW"
                    ''')
                }
            }
        }
        stage('setup & run tests'){
            steps{
                dir("${env.ANSIBLE_PROJ_ROOT_DIR}"){
                sh("""
                    . ./setup.sh
                    python3 runner.py --${env.condition} -p ${env.product} -v ${env.version} -o ${env.os} -f ${env.feature} -l ${env.limittohost}               
                    """)
                }
            }
        }
        stage('Post Actions'){
        environment{
                lastFile = sh (
                script: "ls -Art $env.ANSIBLE_PROJ_LOG_DIR | tail -n 1",
                returnStdout: true
                ).trim()
                custombuildName = sh (
                script: "echo ${env.lastFile} | sed 's/ *_[1-9][0-9][0-9][0-9]-[0-9][1-9]-[0-9][1-9]-[0-9][0-9]:[0-9][0-9]:[0-9][0-9].log//g'",
                returnStdout: true
                ).trim()
            }
            steps{
                dir("${env.ANSIBLE_PROJ_LOG_DIR}"){
                sh("""
                    echo ${env.lastFile}
                    """)
                script{
                    currentBuild.displayName= "${env.BUILD_DISPLAY_NAME}_${env.custombuildName}"
                }
                archiveArtifacts artifacts: "${env.lastFile}", caseSensitive: false, followSymlinks: false, onlyIfSuccessful: true, fingerprint: true
                }
            }
        }
    }
}