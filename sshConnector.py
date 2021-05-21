# Requires paramiko

import paramiko
import os

username1 = 'root'
username2 = 'admin'
username3 = 'user'
password = 'password'
ipaddresses = '192.168.0.X','192.168.0.X'

for ip in ipaddresses:
    try: 
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, username=username1, password=password)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('hostname')
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 

        for line in ssh_stdout:
            print(line.strip())
    except:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip, username=username2, password=password)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('hostname')
            exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 

            for line in ssh_stdout:
                print(line.strip())
        except:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname=ip, username=username3, password=password)
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('hostname')
                exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 

                for line in ssh_stdout:
                    print(line.strip())