import paramiko
import sys
import getpass

host = sys.argv[1]
port = 22
username = sys.argv[2]
senha = getpass.getpass('Digite a senha: ')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(host, port, username, senha)

stdin, stdout, stderr = ssh.exec_command('ls') #retorna 3 valores: STDIN, STDOUT,STDERR 
#STDIN = o valor do comando que enviou
#STDOUT = o valor da saido do comando

print(stdout.read())

ssh.close()


