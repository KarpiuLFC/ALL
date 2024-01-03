import paramiko
import getpass
import time
import re

host = '172.30.115.231'
user = 'uszczra'
haslo = getpass.getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=haslo, allow_agent=False,look_for_keys=False)
remote = client.invoke_shell()
print('Logged')
remote.send("terminal length 0\n")
##output = remote.recv(6000)
#print(output)
#print((output).decode('ascii'))
time.sleep(1)
remote.send("show interface status | exc connected\n")
time.sleep(5)
interface = remote.recv(10000)
print((interface).decode('ascii'))
client.close()