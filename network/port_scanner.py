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

print("There are " + str(len(all_devices)) + " devices in the range")
#print(all_devices)

for device in all_devices: # Loop through   devices
    ip = device.get("ip", "") # get value of the key "ip"
    for port in range (23, 24): # only port 23
        dest = (ip, port) # Combine ip and port number to form dest object
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # port scanner tool
                sock.settimeout(3) # add 3 seconds pause to socket application
                connection = sock.connect(dest) #
                print(f"On {ip}, port {port} is open!") # Informational
                net_connect = ConnectHandler(**device) # create a netmiko ConnectHandler object
                if net_connect == False:
                    print("Username or password dont match")
                    break
                config_commands = ['vlan 200', 'name vlan_200'] # netmiko config_commands
                net_connect.send_config_set(config_commands) # send netmiko send_config_set
                output = net_connect.send_command("show run | inc vlan_200")# send a show command to
                print()# Informational
                print('-' * 80) # Displayed information separator line
                print(output) # Informational  
                print('-' * 80) # Displayed information separator line
                print()# Informational
                net_connect.disconnect() # close netmiko connection
        except:
            print(f"On {ip}, port {port} is closed.")



    