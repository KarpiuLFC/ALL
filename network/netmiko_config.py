import confirm_password
from netmiko import ConnectHandler
import time

confirm_password.get_credentials() # Run get_credentials() function

all_devices = [] #Define empty list of switches

index = 1 #Start of indexing
file = open("lab_routers.txt", "r", encoding="utf8", errors='ignore') #open file
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
index = 1

for device in all_devices:
    ip = device.get("ip", "")
    print(ip)
    try:
        net_connect = ConnectHandler(**device) # create a netmiko ConnectHandler object
        net_connect.enable()
        output1 = net_connect.send_command("show inter description")# send a show command to
        print()# Informational
        print('-' * 40 + ip + '-' * 40) # Displayed information separator line
        print(output1) # Informational      
        #print("No VLAN 200 on " + ip)
        print('-' * 93) # Displayed information separator line
        print()# Informational
        print("Creating Tu0 interface")
        print()
        config_commands = ('int Tu0','description DMVPN tunnel interface',f'ip address 192.168.0.{index} 255.255.255.0')
        #config_commands = ['no int Tu0'] # netmiko config_commands
        net_connect.send_config_set(config_commands) # send netmiko send_config_set
        time.sleep(3)
        output2 = net_connect.send_command('show inter description')# send a show command to
        time.sleep(3)
        output3 = net_connect.send_command('show ip inter brief')
        time.sleep(3)
        print()# Informational
        print('-' * 40 + ip + '-' * 40) # Displayed information separator line
        print(output2) # Informational 
        print()
        print(output3)     
        print('-' * 93) # Displayed information separator line
        print()# Informational
        net_connect.disconnect() # close netmiko connection
    except Exception as e:
        print("Cannot login to device " + ip)
        print(e)
        error_ssh = net_connect = ConnectHandler(**device) # create a netmiko ConnectHandler object
        print(error_ssh)
    index += 1
        
        