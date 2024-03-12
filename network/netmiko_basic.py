import netmiko 
import getpass
import time

device1 = { # define device 
'device_type': 'cisco_ios',
'ip': input('IP Address : '),
'username': input('Enter username : '),
'password': getpass.getpass('SSH password : '),
}

net_connect = netmiko.ConnectHandler(**device1) # required netmiko command that let us ssh to device, openning a ssh session
print ("logged " + str(device1.get("ip"))) # some printed or label, whatever what we want - not mandatory
net_connect.send_command("show version | inc uptime \n")  # send a commend to device
set=net_connect.send_command("show version | inc uptime \n") # set a command as a variable to simplify usage 
time.sleep(3) # need to specify sleep time to allow process command on the device, other way netmiko.exceptions.ReadTimeout error could appear
print(set) # print output of defined command
net_connect.disconnect # closing ssh session