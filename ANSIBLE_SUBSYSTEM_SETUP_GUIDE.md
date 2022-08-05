# Ansible subsystem controller setup guide:

This demos the setup of ansible subsytem on a Linux(Centos/RHEL) environment which can be used for automating the software provisioning and configure environments on test/build environments. <br />


**Guide for setting up ansible subsystem controller on a Linux environment :**
1. **_Install below packages:_** -> *minimum version of python3.6 is required for ansible to work*
> &emsp; yum install python3 python3-virtualenv<br /> 
2. Create a virtual environment and install ansible in the virtual environment-> *follow Detailed Instructions mentioned below to complete the ansible setup in your ansible server controller*

  
**Detailed Instructions:**<br />

**Step 1**: Verify that Python3 is installed on Ansible control node
>       sudo dnf install python3
>       sudo alternatives --set python /usr/bin/python3
**Step 2**: Create a virtual environment to begin with.
>       sudo dnf install python3-virtualenv
>       virtualenv ansible-subsystem
>       (*provide any desired name for your vitual environment)
**Step 3**: List the directories
>        [<user>@oransicentos8 ~]# ls
>        ansible-subsystem  env  initial-setup-ks.cfg
**Step 4**: Activate the virtual environment
>        [<user>@oransicentos8 ~]# source ansible-subsystem/bin/activate
**Step 5**: Verify the python version in the virtual environment
>        (ansible-subsystem) [<user>@oransicentos8 ~]$ python --version
>        Python 3.6.8
**Step 6**: Install Ansible in the virtual envrionment
>        (ansible-subsystem) [<user>@oransicentos8 ~]# pip install ansible
**Step 7**: Verify ansible version (make sure minimum version atleast 2.9)
>        (ansible-subsystem) [<user>@oransicentos8 ~]$ ansible --version
>        ansible 2.9.7
>        config file = /etc/ansible/ansible.cfg
>        configured module search path = ['/home/<user>/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
>        ansible python module location = /home/<user>/ansible-subsystem/lib/python3.6/site-packages/ansible
>        executable location = /home/<user>/ansible-subsystem/bin/ansible
>        python version = 3.6.8 (default, Nov 21 2019, 19:31:34) [GCC 8.3.1 20190507 (Red Hat 8.3.1-4)]
**Step 8**: If in case config file = None, then follow the below steps to set up the ansible.cfg and hosts. host file is required to configure the host servers that you would like to establish connections with. Run the below command,
>        (ansible-subsystem) [<user>@oransicentos8 ~]$ ansible-config view
**Step 9**: Now Clone the current repo [https://alm.actian.com/bitbucket/scm/~akarunak/ansible_controller.git] to /etc/ansible directory<br />
**Step 10**: Run the command to check whether OpenSSH server daemon has started and server is listening on port successfully,
>        [<user>@oransicentos8 ~]$ sudo systemctl status sshd
**Step 11**: And check whether the sshd connection is Active and in running state and check whether the session is opened with permissions enabled for user root. If permission are not enabled and fails for root user with below error,
>        May 12 20:15:17 oransicentos8 sshd[31140]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=10.5.20.99 user=root
>        May 12 20:15:17 oransicentos8 sshd[31140]: pam_succeed_if(sshd:auth): requirement "uid >= 1000" not met by user "root"
>        May 12 20:15:19 oransicentos8 sshd[31140]: Failed password for root from 10.5.20.99 port 29101 ssh2
>        May 12 20:15:19 oransicentos8 sshd[31140]: Connection closed by authenticating user root 10.5.20.99 port 29101 [preauth]
>        May 12 20:15:31 oransicentos8 sshd[31143]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=10.5.20.99 user=root
>        May 12 20:15:31 oransicentos8 sshd[31143]: pam_succeed_if(sshd:auth): requirement "uid >= 1000" not met by user "root"
>        May 12 20:15:33 oransicentos8 sshd[31143]: Failed password for root from 10.5.20.99 port 29139 ssh2
>        May 12 20:15:35 oransicentos8 sshd[31143]: Connection closed by authenticating user root 10.5.20.99 port 29139 [preauth]
>        May 13 03:31:27 oransicentos8 systemd[1]: Stopping OpenSSH server daemon...
>        May 13 03:31:27 oransicentos8 systemd[1]: Stopped OpenSSH server daemon.
**Step 12**: Restart the systemctl sshd service, and Wait a while and make sure the pam_unix(sshd:session): session opened for user
>       [<user>@oransicentos8 ~]$ sudo systemctl start sshd
>       [<user>@oransicentos8 ~]$ sudo systemctl enable sshd
>       [<user>@oransicentos8 ~]$ sudo systemctl status sshd
>        ● sshd.service - OpenSSH server daemon
>           Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset>
>           Active: active (running) since Wed 2020-05-13 03:31:48 EDT; 21min ago
>             Docs: man:sshd(8)
>                   man:sshd_config(5)
>         Main PID: 5901 (sshd)
>          >          Tasks: 1 (limit: 26213)
>           Memory: 3.4M
>           CGroup: /system.slice/sshd.service
>                   └─5901 /usr/sbin/sshd -D -oCiphers=aes256-gcm@openssh.com,chacha20-p>
>        
>        May 13 03:31:48 oransicentos8 systemd[1]: Starting OpenSSH server daemon...
>        May 13 03:31:48 oransicentos8 sshd[5901]: Server listening on 0.0.0.0 port 22.
>        May 13 03:31:48 oransicentos8 sshd[5901]: Server listening on :: port 22.
>        May 13 03:31:48 oransicentos8 systemd[1]: Started OpenSSH server daemon.
>        May 13 03:52:48 oransicentos8 sshd[6649]: Accepted password for <user> from 1>
>        May 13 03:52:48 oransicentos8 sshd[6649]: pam_unix(sshd:session): session opene>
>        lines 1-17/17 (END)
>        ● sshd.service - OpenSSH server daemon
>           Loaded: loaded (/usr/lib/systemd/system/sshd.service; enabled; vendor preset: enabled)
>           Active: active (running) since Wed 2020-05-13 03:31:48 EDT; 21min ago
>             Docs: man:sshd(8)
>                   man:sshd_config(5)
>         Main PID: 5901 (sshd)
>            Tasks: 1 (limit: 26213)
>           Memory: 3.4M
>           CGroup: /system.slice/sshd.service
>                   └─5901 /usr/sbin/sshd -D -oCiphers=aes256-gcm@openssh.com,chacha20-poly1305@openssh.com,aes256-ctr,aes256-cbc,aes128-gcm@openssh.com,aes128-ctr,aes1>
>        
>        May 13 03:31:48 oransicentos8 systemd[1]: Starting OpenSSH server daemon...
>        May 13 03:31:48 oransicentos8 sshd[5901]: Server listening on 0.0.0.0 port 22.
>        May 13 03:31:48 oransicentos8 sshd[5901]: Server listening on :: port 22.
>        May 13 03:31:48 oransicentos8 systemd[1]: Started OpenSSH server daemon.
>        May 13 03:52:48 oransicentos8 sshd[6649]: Accepted password for <user> from 10.5.248.139 port 60719 ssh2
>        May 13 03:52:48 oransicentos8 sshd[6649]: pam_unix(sshd:session): session opened for user <user> by (uid=0)
**Step 13**: create ssh-keygen
>       [<user>@oransicentos8 ~]$ ssh-keygen
>       [<user>@oransicentos8 ansible]$ ssh-keygen
>       Generating public/private rsa key pair.
>       Enter file in which to save the key (/home/<user>/.ssh/id_rsa): 
>       /home/<user>/.ssh/id_rsa already exists.
>       Overwrite (y/n)? y
>       Enter passphrase (empty for no passphrase): 
>       Enter same passphrase again: 
>       Your identification has been saved in /home/<user>/.ssh/id_rsa.
>       Your public key has been saved in /home/<user>/.ssh/id_rsa.pub.
>       The key fingerprint is:
>       SHA256:WZsirFvp+82Mcwaiz67j99KGOfw/UKAOP8ZsS3NTJF8 <user>@oransicentos8
>       The key's randomart image is:
>       +---[RSA 3072]----+
>       | |
>       | o . E |
>       | . =.. |
>       | ... o+o |
>       | *o Soo |
>       | .%o=. |
>       | .*oX + |
>       | o=O +=+ |
>       | .+**O===. |
>       +----[SHA256]-----+
**Step 14**: Copy the generated SSH key to the remote node which you want to control,
>       [<user>@oransicentos8 ~]$ ssh-copy-id <user@widowshost_ipaddress>
**Step 15**: Check whether your ping to the local machine is working fine without any issues as below,
>       (ansible-subsystem) [<user>@oransicentos8 ~]$ ansible localhost -m ping
>       localhost | SUCCESS => {
>       "changed": false,
>       "ping": "pong"
>       }
**Step 16**: Recheck on inventory host values specified by the user for remote server configurations,
>       (ansible-subsystem) [<user>@oransicentos8 ~]$ ansible-inventory --list
** This should return the below similar JSON format if hosts are specified ** -> *replace the below hostip1, host_ip2 with the ip addresses of your remote machine that you want to control*
>       {
>       "_meta": {
>       "hostvars": {
>       "<host_ip1>": {
>       "ansible_password": "<password>",
>       "ansible_user": "<username>",
>       },
>       "<host_ip2>": {
>       "ansible_password": "<password>",
>       "ansible_user": "<username>",
>       }
>       }
>       },
>       "all": {
>       "children": [
>       "ungrouped",
>       "linuxhost"
>       ]
>       },
>       "linuxhost": {
>       "hosts": [
>       "<host_ip1>",
>       "<host_ip2>"
>       ]
>       }
>       }
**Step 17**: Now use ansible to ping the remote hosts and check whether connection is established between the ansible server and remote windows host machine,
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ ansible -i /etc/ansible/hosts -m win_ping all
>       <host_ip1> | SUCCESS => {
>       "changed": false,
>       "ping": "pong"
>       }
>       <host_ip2> | SUCCESS => {
>       "changed": false,
>       "ping": "pong"
>       }  
*Note: if you are not able to successfully ping your remote windows nodes then continue with the below setup*<br />
## Setup for managing Windows hosts using ansible playbooks 
**Step 18**: Configure the ansible Control Machine with OpenSSL
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ pip install pyOpenSSL --upgrade
**Step 19**: Install pywinrm with support for basic, certificate, and NTLM auth
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ pip install pywinrm
**Step 20**: Configuring Windows node machines<br /> 
>  For configuring our Windows 10/11, Windows Server 16/19/22 remote host system to connect with the Ansible Control node. We need to install the WinRM listener- short for Windows Remote – which will allow the connection between the Windows host system and the Ansible server. Before we do so, the Windows host system needs to fulfill a few requirements for the installation to succeed,

1.  Your Windows host system should be Windows 7 or later. For Servers, ensure that you are using Windows Server 2008 and later versions.
2.  Ensure your system is running .NET Framework 4.0 and later.
3.  Windows PowerShell should be Version 3.0 & later
4.  With all the requirements met, now follow the steps stipulated below:<br />
i.  Download the https://github.com/jborean93/ansible-windows/blob/master/scripts/Install-WMF3Hotfix.ps1 file to the desktop of the remote windows host VM and run it on an elevated powershell window.<br />
ii.  Download the https://github.com/jborean93/ansible-windows/blob/master/scripts/Upgrade-PowerShell.ps1 file to the desktop of the remote windows host VM and run the script on an elevated powershell window.<br />
iii.  Download the https://github.com/ansible/ansible/blob/devel/examples/scripts/ConfigureRemotingForAnsible.ps1 file to the desktop of the remote windows host VM and run it using powershell 3.0 or greater version as an administrator. Make sure a self signed SSL certificate is generated.<br />
5.  Setup OpenSSH if not installed and running on the target Windows machine.<br /> On a windows powershell run the below commands,
> 1. Set-ExecutionPolicy RemoteSigned<br />
> 2. Get-WindowsCapability -Online | ? Name -like 'OpenSSH.Server*'<br />
>   &emsp;*******if state: not installed then run the below commands,<br />
> 3. dism /Online /Add-Capability /CapabilityName:OpenSSH.Server<br />
> 4. Get-WindowsCapability -Online | ? Name -like 'OpenSSH.Server*'<br />
>   &emsp;*******state: should be installed now<br />
> 5. Get-Service -Name *ssh*<br />
> 6. Start-Service sshd<br />
> 7. Set-Service -Name sshd -StartupType 'Automatic'<br />
> 8. Start-Service ‘ssh-agent’<br />
> 9. Set-Service -Name ‘ssh-agent’ -StartupType 'Automatic'<br />
<br />

**Step 21**: Checking for successfull connections:<br />
1. Navigate to /etc/ansible directory on your ansible server. And update the hosts file with the required host file details, update it as per your requirement.<br />
>       [winhost] 
>       <serverip1> 
>       <serverip2>
>       [winhost:vars] 
>       ansible_user=<username> 
>       ansible_password=<password> 
>       ansible_connection=winrm 
>       ansible_winrm_server_cert_validation=ignore
2. Run the below command to verify whether you are able to ping to hostservers from ansible,<br />
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ ansible -i /etc/ansible/hosts -m win_ping <hostname>
>       <host_ip1> | SUCCESS => {
>       "changed": false,
>       "ping": "pong"
>       }
>       <host_ip2> | SUCCESS => {
>       "changed": false,
>       "ping": "pong"
>       }
  
**Note**: ‘win_ping’ is used here for windows host connections, if it is unix host machine that we are trying to ping, then we are suppose to use ‘ping’ instead of win_ping.<br />
  
**Step 22**: Based on title specified in the hosts file you can ping both windows hosts and unix hosts continuously,
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ ansible -i /etc/ansible/hosts <enterlinuxhostnamehere> -m ping
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ ansible -i /etc/ansible/hosts <enterwinhostnamehere> -m win_ping
**Step 23**: Try running remote commands
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ ansible -i /etc/ansible/hosts <enterwinhostnamehere> -m win_command -a "cmd /c dir C:\\"
>       <host_ip1> | CHANGED | rc=0 >>
>       Volume in drive C has no label.
>        Volume Serial Number is 2A92-F6EB
>       Directory of C:\
>       
>       05/08/2020 02:08 AM <DIR> cygwin64
>       04/30/2020 05:43 AM <DIR> Jenkins
>       09/15/2018 12:19 AM <DIR> PerfLogs
>       05/08/2020 12:43 PM <DIR> Program Files
>       05/08/2020 12:56 PM <DIR> Program Files (x86)
>       03/26/2020 01:22 AM <DIR> Users
>       05/08/2020 01:04 PM <DIR> Windows
>       0 File(s) 0 bytes
>       7 Dir(s) 186,558,099,456 bytes free
>       (ansible-subsystem) [<user>@oransicentos8 bin]$ ansible -i /etc/ansible/hosts <enterlinuxhostnamehere> -m command -a "sudo apt-get install vim"
