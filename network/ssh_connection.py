import paramiko
import getpass
import time

host = '10.244.52.165'
user = 'netadmin'
haslo = getpass.getpass()

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=haslo, allow_agent=False,look_for_keys=False, timeout=60)
remote = client.invoke_shell()
device = remote.recv(1000)
print('Logged to ' + device.decode('utf-8').strip())
print()
time.sleep(1)
remote.send("show version | inc uptime\n")
time.sleep(5)
uptime = remote.recv(1000)
print((uptime).decode('ascii'))
client.close()