import time # import time module
import paramiko # import paramiko library
from datetime import datetime # import datetime module from datetime library
import confirm_password

confirm_password.get_credentials() # Run get_credentials() function
        
file=open("switches.txt", "r", encoding="utf8", errors='ignore')
for line in file.readlines():
    t_ref = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Time reference to be used for file name
    print(t_ref)
    print()
    ip=line.strip() #remove unnecessary characters
    print("Logged to " + ip)
    ssh_client = paramiko.SSHClient()# Initiate paramiko SSH client session as ssh_client
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Accept missing host key policy
    ssh_client.connect(hostname=ip,username=confirm_password.user,password=confirm_password.password, allow_agent=False,look_for_keys=False, timeout=60) # SSH connection with credentials
    show_vers = ssh_client.invoke_shell()
    time.sleep(1)   
    show_vers.send("show version | inc Processor\n")
    time.sleep(3)
    device = show_vers.recv(60000)
    print(device.decode('utf-8')) # remove all unwanted characters  
    ssh_client.close # Close SSH session
    print("Kicked out from " + ip)
    print("-" * 40, "END", "-" * 40 )
file.close()