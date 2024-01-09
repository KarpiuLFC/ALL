import re # import regular expression module
import time # import time module
import paramiko # import paramiko library
from datetime import datetime # import datetime module from datetime library
import confirm_password

confirm_password.get_credentials() # Run get_credentials() function

def terminal_lenght():
    terminal = ssh_client.invoke_shell()
    terminal.send("terminal length 0\n")
    time.sleep(1)

def show_version():
    show_vers = ssh_client.invoke_shell()
    show_vers.send("show version\n")
    time.sleep(3)
    device = show_vers.recv(65000)
    print(device.decode('utf-8'))

start_timer = time.mktime(time.localtime()) # Start time
#print(confirm_password.user)
#print(confirm_password.password)
file=open("list.txt", "r", encoding="utf8", errors='ignore')
for line in file.readlines():
    t_ref = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Time reference to be used for file name
    print(t_ref)
    ip=line.strip() #remove unnecessary characters
    ssh_client = paramiko.SSHClient()# Initiate paramiko SSH client session as ssh_client
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Accept missing host key policy
    ssh_client.connect(hostname=ip,username=confirm_password.user,password=confirm_password.password, allow_agent=False,look_for_keys=False) # SSH connection with credentials
    print("Logged to " + ip)
    #terminal_lenght()
    show_version()
    ssh_client.close # Close SSH session
    print("Kicked out from " + ip)
    print("-" * 40, "END", "-" * 40 )
file.close()