import netmiko
import getpass

device1 = {
'device_type': 'cisco_ios',
'ip': input('IP Address : '),
'username': input('Enter username : '),
'password': getpass.getpass('SSH password : '),
}

net_connect = netmiko.ConnectHandler(**device1)
print ("logged " + str(device1.get("ip")))
net_connect.send_command("show version | inc uptime\n")
set=net_connect.send_command("show version | inc uptime\n")
print(set)
net_connect.disconnect