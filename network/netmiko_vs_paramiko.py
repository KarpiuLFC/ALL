import paramiko
import getpass
import time
import netmiko 

host = '10.244.52.165'
user = 'netadmin'
haslo = getpass.getpass()
print()
print('HERE IS AN EXAMPLE OF PARAMIKO')
print()
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=haslo, allow_agent=False,look_for_keys=False, timeout=60)
remote = client.invoke_shell()
device = remote.recv(1000)
print('Logged to ' + device.decode('utf-8').strip())
print()
time.sleep(1)
remote.send("show version \n")
time.sleep(5)
vers = remote.recv(10000)
print((vers).decode('ascii'))
client.close()

device1 = { # define device 
'device_type': 'cisco_ios',
'ip': '10.244.52.165',
'username': 'netadmin',
'password': haslo,
}
print()
print('HERE IS AN EXAMPLE OF NETMIKO')
print()
net_connect = netmiko.ConnectHandler(**device1) # required netmiko command that let us ssh to device, openning a ssh session
print ("logged " + str(device1.get("ip"))) # some printed or label, whatever what we want - not mandatory
net_connect.send_command("show version \n")  # send a commend to device
set=net_connect.send_command("show version \n") # set a command as a variable to simplify usage 
time.sleep(3) # need to specify sleep time to allow process command on the device, other way netmiko.exceptions.ReadTimeout error could appear
print(set) # print output of defined command
net_connect.disconnect # closing ssh session
