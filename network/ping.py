import os

def icmp_pinger(ip):

   rep = os.system('ping -c 10 ' + ip)

   if rep == 0:

      print(f"{ip} is reachable.") # Print ip is reachable if the device is on the network

   else:

      print(f"{ip} is either offline or icmp is filtered. Exiting.")

      exit() # Exit application if any ip address is unreachable.

print("-"*80)

ip = "8.8.8.8"

if __name__ == "__main__": 
   icmp_pinger(ip) # Run get_credentials() function