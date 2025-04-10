import time # import time module
import paramiko # import paramiko library
from datetime import datetime # import datetime module from datetime library
import confirm_password

confirm_password.get_credentials() # Run get_credentials() function

index = 10 # index for host naming convention

def disable_paging(show_vers): #Disable paging on a Cisco router
    show_vers.send("terminal length 0\n")
    time.sleep(1)# Clear the buffer on the screen
    output = show_vers.recv(1000)
    return output
        
def hostname(): # Create a hostname function
    global conf_host
    ssh_client = paramiko.SSHClient()# Initiate paramiko SSH client session as ssh_client
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Accept missing host key policy
    ssh_client.connect(hostname=ip,username=confirm_password.user,password=confirm_password.password, allow_agent=False,look_for_keys=False, timeout=60) # SSH connection with credentials
    conf_host = ssh_client.invoke_shell()
    conf_host.send(f"copy scp://swupgrade@10.111.128.34/home/swupgrade/images/nxos/nxos.9372PX-E.rpm bootflash:\n \n dir | grep nxos.9372\n \n show file bootflash:nxos.9372PX-E.rpm md5sum\n")
    time.sleep(1)# Clear the buffer on the screen
    ssh_client.close
    output = conf_host.recv(40000)
    print(output.decode('utf-8')) 
    print()

#start_timer = time.mktime(time.localtime()) # Start time

file=open("example.txt", "r", encoding="utf8", errors='ignore')
for line in file.readlines():
    t_ref = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Time reference to be used for file name
    print(t_ref)
    print()
    ip=line.strip() #remove unnecessary characters
    print("Logged to " + ip)
    hostname()   
    print("Kicked out from " + ip)
    print("-" * 40, "END", "-" * 40 )
    index += 10
file.close()