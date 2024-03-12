import socket
import time

with open("lab_routers.txt", newline='') as all_devices:
    x = len(all_devices.readlines()) # check how many lines are in file
    print("There are " + str(x) + " devices in the range: ") #print count of (all_devices)  
    time.sleep(3)
with open("lab_routers.txt", newline='') as all_devices:   
    for device in all_devices: # Loop through   devices
        for port in range (389, 390): # check ports 22-ssh and 23-telnet
            device = device.strip() # remove white spaces
            dest = (device, port) # Combine ip and port number to form dest object
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock: # port scanner tool
                    sock.settimeout(3) # add 3 seconds pause to socket application
                    onnection = sock.connect(dest) #                    
                    print(f"On {device}, port {port} is open!") # Informational
            except:
                print(f"On {device}, port {port} is closed.")
      



    