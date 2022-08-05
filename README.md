[![Build Status](https://alm.actian.com/jenkins/ea/buildStatus/icon?job=ansible-server_codesync)](https://alm.actian.com/jenkins/ea/job/ansible-server_codesync/)

The build status over here highlights whether this code in master repo is in sync with the project repository in the ansible server box. 
# **Usage guide:**<br />

>  For Detailed usage of ansible commands and ansible server box refer jira ticket [OR-5556](https://actian.atlassian.net/browse/OR-5556) <br />

>  For details on setting up a new ansible subsystem controller for managing windows and linux hosts refer [Ansible Subsystem setup guide](https://alm.actian.com/bitbucket/projects/OR/repos/ansible_controller/browse/ANSIBLE_SUBSYSTEM_SETUP_GUIDE.md) <br /> 


**Main Step:** After login to the project folder of ansible server box as refered in ticket [OR-5556](https://actian.atlassian.net/browse/OR-5556) <br />
>  source setup.sh

## *Platform Windows*
------------------

### *_OpenROAD specific_:*

**Step1**: To perform role specific installs/upgrades
> cd to $ANSIBLE_PROJ_PLATFORM_WINDOWS

**Step 2**: To install an OpenROAD patch from staging environment specify the ansible-playbook command in the below format
>  syntax: ansible-playbook -i [inventoryname] install-openroad.yml -l [remotehostname] -v --extra-vars "{'as_user':'[username]','filepath':'[filepath]','filename':'[filename]','feature':'[featurename]'}" --tags "[tagstobeconsidered]" --skip-tags "[tagstobeskipped]"

<u>**Command References for Install/Upgrade of an OR patch:**</u><br />
<u>*Sample:*</u><br />
*Install :* **p15701**<br />
*Upgrade to :* **p15719**<br />

| Scenarios| Purpose| Product | Component | Version	| Platform | commands | Notes |
| --------|---------|-------|--------|---------|-------|--------|---------|
|To perform clean install of patch |  deployment	| OR	| sanet	| 11.2	| a64.win | ansible-playbook -i inventory install-openroad.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanet'}" --tags "or112, install" --skip-tags "debug, installoptions" | Will do a clean install of patch 15701 sanet using ormsiexec11.bat |
To perform an upgrade from lower com/patch edition to recent patch   | 	deployment|	OR|	sanet|	11.2|	a64.win|ansible-playbook -i inventory install-openroad.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15719', 'filename':'openroad-11.20.20008-win-x86_64-p15719-a.zip','feature':'sanet'}" --tags "or112, upgrade" --skip-tags "debug, installoptions, cleaninstall"|Will Upgrade patch 15701 sanet earlier installed to 15719 sanet using ormsiexec11.bat |
To perform clean install of patch   |        	deployment|	OR|	sanetruntime|	11.2|	a64.win|	ansible-playbook -i inventory install-openroad.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanetruntime'}" --tags "or112, install" --skip-tags "debug, installoptions"|	"Will do a clean fresh install of patch 15701 sanetruntime using ormsiexec11.bat "|
To perform an upgrade from lower com/patch edition to recent patch   | 	deployment|	OR|	sanetruntime|	11.2|	a64.win	|ansible-playbook -i inventory install-openroad.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15719', 'filename':'openroad-11.20.20008-win-x86_64-p15719-a.zip','feature':'sanetruntime'}" --tags "or112, upgrade" --skip-tags "debug, installoptions, cleaninstall"|	Will Upgrade patch 15701 sanetruntime earlier installed to 15719 sanetruntime using ormsiexec11.bat |

**Note:** commands to be run from ansible server machine<br /> 
<br />


### *_Loadnrun specific_:*


**Step1**: To perform role specific installs/upgrades

> cd to $ANSIBLE_PROJ_PLATFORM_WINDOWS

**Step 2**: To install a Loadnrun patch from staging environment specify the ansible-playbook command in the below format
>  syntax: ansible-playbook -i [inventoryname] install-loadnrun.yml -l [remotehostname] -v --extra-vars "{'as_user':'[username]','filepath':'[filepath]','filename':'[filename]','feature':'[featurename]'}" --tags "[tagstobeconsidered]" --skip-tags "[tagstobeskipped]"
<br />

<u>**Command References for Install/Upgrade of a LNR patch:**</u><br />
<u>*Sample:*</u><br />
*Install :* **p15701**<br />
*Upgrade to :* **p15719**<br />

| Scenarios| Purpose| Product | Component | Version | Platform | commands | Notes |
| --------|---------|-------|--------|---------|-------|--------|---------|
|To perform clean install of patch |  deployment  | LNR  | sanet | 11.2  | a64.win | ansible-playbook -i inventory install-loadnrun.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'loadnrun-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanet'}" --tags "lnr112, install" --skip-tags "debug, installoptions" | Will do a clean install of patch 15701 sanet using ormsiexec11.bat |
To perform an upgrade from lower com/patch edition to recent patch   |  deployment| LNR| sanet|  11.2| a64.win|ansible-playbook -i inventory install-loadnrun.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15719', 'filename':'loadnrun-11.20.20008-win-x86_64-p15719-a.zip','feature':'sanet'}" --tags "lnr112, upgrade" --skip-tags "debug, installoptions, cleaninstall"|Will Upgrade patch 15701 sanet earlier installed to 15719 sanet using ormsiexec11.bat |
To perform clean install of patch   |         deployment| LNR| sanetruntime| 11.2| a64.win|  ansible-playbook -i inventory install-loadnrun.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'loadnrun-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanetruntime'}" --tags "lnr112, install" --skip-tags "debug, installoptions"| "Will do a clean fresh install of patch 15701 sanetruntime using ormsiexec11.bat "|
To perform an upgrade from lower com/patch edition to recent patch   |  deployment| LNR| sanetruntime| 11.2| a64.win |ansible-playbook -i inventory install-loadnrun.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15719', 'filename':'loadnrun-11.20.20008-win-x86_64-p15719-a.zip','feature':'sanetruntime'}" --tags "lnr112, upgrade" --skip-tags "debug, installoptions, cleaninstall"|  Will Upgrade patch 15701 sanetruntime earlier installed to 15719 sanetruntime using ormsiexec11.bat |

**Note:** commands to be run from ansible server machine<br /> 
<br />


### *_For Managing All products_:*

**Step1**: To Perform Install/uprades of all products from project root directory

> cd to $ANSIBLE_PROJ_ROOT_DIR

<u>**Installing patches using python wrapper script runner.py:**</u><br />

| Scenarios| Purpose| Product | Component | Version	| Platform | commands | Notes |
| --------|---------|-------|--------|---------|-------|--------|---------|
|To install latest patch found on staging |  test / CI / deploy	| OR	| sanet	| 11.2	| a64.win | python3 runner.py --install_latestpatch -p OR -v 11.2.0 -o a64.win -f sanet -l [hostname]| Will do a clean install of latest patch from staging using ormsiexe11.bat |
|To install an immediate previous patch found on staging |  test / CI	| OR	| sanet	| 11.2	| a64.win | python3 runner.py --install_previouspatch -p OR -v 11.2.0 -o a64.win -f sanet -l [hostname] | Will do a clean install of an immediate previous patch from staging using ormsiexe11.bat |
|To upgrade a path to latest patch found on staging |  test / CI / deploy	| OR	| sanet	| 11.2	| a64.win | python3 runner.py --upgrade_tolatestpatch -p OR -v 11.2.0 -o a64.win -f sanet -l [hostname] | Will upgrade the old patch installed to latest patch found in staging using ormsiexe11.bat |
|To upgrade all the previous patches found on staging to latest patch |  test / CI	| OR	| sanet	| 11.2	| a64.win | python3 runner.py --upgradeall_to_latestpatch -p OR -v 11.2.0 -o a64.win -f sanet -l [hostname] | if there are patches A, B, C and D found on staging , it will test the upgrade of patches A to D , B to D and C to D using ormsiexe11.bat |

**Note:** commands to be run from ansible server machine<br />

<u>**Command References for Install/Upgrade of an OR patch using ansible:**</u><br />
<u>*Sample:*</u><br />
*Install :* **p15701**<br />
*Upgrade to :* **p15719**<br />

| Scenarios| Purpose| Product | Component | Version	| Platform | commands | Notes |
| --------|---------|-------|--------|---------|-------|--------|---------|
|To perform clean install of patch |  deployment	| OR	| sanet	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanet'}" --tags "or, or112, install" --skip-tags "debug, installoptions, lnr" | Will do a clean fresh install of patch 15701 sanet using ormsiexec11.bat |
To perform an upgrade from lower com/patch edition to recent patch   | 	deployment|	OR|	sanet|	11.2|	a64.win|ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15719', 'filename':'openroad-11.20.20008-win-x86_64-p15719-a.zip','feature':'sanet'}" --tags "or, or112, upgrade" --skip-tags "debug, installoptions, lnr, cleaninstall"|Will Upgrade patch 15701 sanet earlier installed to 15719 using ormsiexec11.bat |
To perform clean install of patch   |        	deployment|	OR|	sanetruntime|	11.2|	a64.win|	ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanetruntime'}" --tags "or, or112, install" --skip-tags "debug, installoptions, lnr"|	"Will do a clean fresh install of patch 15701 sanetruntime using ormsiexec11.bat "|
To perform an upgrade from lower com/patch edition to recent patch   | 	deployment|	OR|	sanetruntime|	11.2|	a64.win	|ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15719', 'filename':'openroad-11.20.20008-win-x86_64-p15719-a.zip','feature':'sanetruntime'}" --tags "or, or112, upgrade" --skip-tags "debug, installoptions, lnr, cleaninstall"|	Will Upgrade patch 15701 sanetruntime earlier installed to 15719 sanetruntime using ormsiexec11.bat |

**Note:** commands to be run from ansible server machine<br />

<u>**Additional Command References (testing specific):**</u><br />
<u>*Sample:*</u><br />
*Install :* **p15701**<br />
*Uninstall :* **p15701**<br />

| Scenarios| Purpose| Product | Component | Version	| Platform | commands | Notes |
| --------|---------|-------|--------|---------|-------|--------|---------|
|To perform install and uninstall of OpenROAD com/patch editions sequencially |  test	| OR	| sanet	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanet'}" --tags "or, or112, install, uninstall" --skip-tags "debug, reinstall, lnr" | Will do a clean install of patch 15701 and then uninstall the same using ormsiexec11.bat |
To perform install and uninstall and reinstall of OpenROAD com/patch editions sequencially | test	| OR	| sanet	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanet'}" --tags "or, or112, install, uninstall, reinstall" --skip-tags "debug, lnr" | Will do a clean install of patch 15701, uninstall it and then reinstall it back using ormsiexec11.bat |
To perform uninstall of OpenROAD com/patch editions only (provided you know the patch that is installed) |  test	| OR	| sanet	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanet'}" --tags "or, or112, uninstall" --skip-tags "debug, install, reinstall, lnr" | Will do an uninstall of the patch 15701 |
To perform install and uninstall of OpenROAD com/patch editions sequencially |  test	| OR	| sanetruntime	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanetruntime'}" --tags "or, or112, install, uninstall" --skip-tags "debug, reinstall, lnr" | Will do a clean install of patch 15701 and then uninstall it using ormsiexec11.bat |
To perform install and uninstall and reinstall of OpenROAD com/patch editions sequencially | test	| OR	| sanetruntime	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanetruntime'}" --tags "or, or112, install, uninstall, reinstall" --skip-tags "debug, lnr" | Will do a clean install of patch 15701 , uninstall it and then reinstall it back using ormsiexec11.bat |
To perform uninstall of OpenROAD com/patch editions only (provided you know the patch that is installed) | test	| OR	| sanetruntime	| 11.2	| a64.win | ansible-playbook -i inventory/hosts $ANSIBLE_PROJ_PLATFORM_WINDOWS/main.yml -l usau-or-dlw10 -v --extra-vars "{'as_user':'ingres','filepath':'\\usau-engfs01\staging\OpenROAD\OR_11.2.0\a64.win\p15701', 'filename':'openroad-11.20.20007-win-x86_64-p15701-a.zip','feature':'sanetruntime'}" --tags "or, or112, uninstall" --skip-tags "debug, install, reinstall, lnr" | Will do an uninstall of the patch 15701 |

**Note:** commands to be run from ansible server machine<br />
<br/>