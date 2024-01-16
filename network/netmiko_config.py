import confirm_password
import re
from netmiko import ConnectHandler
import time
import socket

confirm_password.get_credentials() # Run get_credentials() function

all_devices = [] #Define empty list of switches

index = 1 #Start of indexing
file = open("list.txt", "r", encoding="utf8", errors='ignore') #open file
for line in file.readlines():
        address=line.strip() #Remove white spaces
        d="ip"+ str(index) #Combine ip(index)
        print('='*40 +d+"="+address+'='*40)
        device = {
            'device_type': 'cisco_ios',
            'ip': address,
            'username': confirm_password.user,
            'password': confirm_password.password
            }
        #print(device)
        all_devices.append(device)
        index += 1
file.close()
def all():
    print("There are " + str(len(all_devices)) + " devices in the range") #print(all_devices)
    
all()

for device in all_devices:
    ip = device.get("ip", "")
    print(ip)
    try:
        net_connect = ConnectHandler(**device) # create a netmiko ConnectHandler object
        net_connect.enable()
        config_commands = ['no vlan 200'] # netmiko config_commands
        net_connect.send_config_set(config_commands) # send netmiko send_config_set
        time.sleep(3)
        output = net_connect.send_command("show vlan brief | inc vlan_200")# send a show command to
        time.sleep(1)
        print()# Informational
        print('-' * 40 + ip + '-' * 40) # Displayed information separator line
        print(output) # Informational      
        #print("No VLAN 200 on " + ip)
        print('-' * 80) # Displayed information separator line
        print()# Informational
        net_connect.disconnect() # close netmiko connection
    except Exception as e:
        print("Cannot login to device " + ip)
        print(e)
        error_ssh = net_connect = ConnectHandler(**device) # create a netmiko ConnectHandler object
        print(error_ssh)
        
        