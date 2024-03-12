import paramiko
import getpass
import time
import re

host = '10.244.52.165'
user = 'netadmin'
haslo = getpass.getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=haslo, allow_agent=False,look_for_keys=False)
remote = client.invoke_shell()
remote.send("show hostname\n")
device = remote.recv(1000)
print('Logged to: ' + device.decode('utf-8').strip())
time.sleep(1)
remote.send("show interface description | inc down\n")
time.sleep(5)
interface = remote.recv(10000)
print()
print("List of interfaces down:")
pattern = re.compile('[A-Z].\d\/\d\/\d.|[A-Z].\d\/\d|[A-Z].\d ') # need to define better regex match
index = pattern.findall((interface).decode('ascii'))
for int in index:
    print(int)
client.close()