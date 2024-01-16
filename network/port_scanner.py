import socket

all_devices = [
'172.30.115.230',
'172.30.115.231',
'172.30.115.192',
'172.30.115.193'
] #Define list of switches

print("There are " + str(len(all_devices)) + " devices in the range: ")
#print(all_devices)

for device in all_devices: # Loop through   devices
        for port in range (22, 24): # check ports 22-ssh and 23-telnet
            dest = (device, port) # Combine ip and port number to form dest object
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # port scanner tool
                    sock.settimeout(3) # add 3 seconds pause to socket application
                    connection = sock.connect(dest) #
                    print(f"On {device}, port {port} is open!") # Informational
            except:
                print(f"On {device}, port {port} is closed.")



    