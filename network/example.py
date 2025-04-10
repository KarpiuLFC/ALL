import time # import time module
import paramiko # import paramiko library
from datetime import datetime # import datetime module from datetime library
import confirm_password

confirm_password.get_credentials() # Run get_credentials() function
        
file=open("example.txt", "r", encoding="utf8", errors='ignore')
for line in file.readlines():
    t_ref = datetime.now().strftime("%Y-%m-%d %H-%M-%S") # Time reference to be used for file name
    print(t_ref)
    print()
    ip=line.strip() #remove unnecessary characters
    print("Logged to " + ip)
    ssh_client = paramiko.SSHClient()# Initiate paramiko SSH client session as ssh_client
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # Accept missing host key policy
    ssh_client.connect(hostname=ip,username=confirm_password.user,password=confirm_password.password, allow_agent=False,look_for_keys=False, timeout=60) # SSH connection with credentials
    conf_host = ssh_client.invoke_shell()
    conf_host.send(f"conf t\n feature bash\n run bash sudo su\n \n cd /tmp\n \n ls | grep bios\n \n cp /bootflash/bios_daemon.dbg /tmp\n \n ls | grep bios\n")
    time.sleep(30)# Clear the buffer on the screen
    ssh_client.close
    output = conf_host.recv(40000)
    print(output.decode('utf-8')) 
    print()
    print("Kicked out from " + ip)
    print("-" * 40, "END", "-" * 40 )
file.close()

