from networkconfgen import NetworkConfGen
import sys

hostname = input("Provide hostname: ") 
vlan_ip = input("Provide VLAN IP address: ") 
mask = input("Provide subnet mask of VLAN: ") 
external = input("Provide external GW IP: ") 
internal = input("Provide internal GW IP: ") 
serial = input("Provide Serial Number: ") 

confgen = NetworkConfGen()

template = """

hostname {{hostname}}

interface Vlan1
 description INSIDE SP-ALARM
 ip address {{ VLAN_IP }} {{VLAN_IP_MASK}}
 no ip redirects
 no ip unreachables
 no ip proxy-arp
 ip tcp adjust-mss 1366
 load-interval 30

ip route 8.8.8.8 255.255.255.255 {{ External_IP }}
ip route 10.240.0.0 255.240.0.0 {{ Internal_IP }}
ip route 10.82.0.0 255.254.0.0 {{ Internal_IP }}
ip route 10.82.0.0 255.254.0.0 {{ Internal_IP }}
ip route 10.82.0.0 255.254.0.0 {{ Internal_IP }}

crypto ipsec security-association replay window-size 1024
!
crypto ipsec transform-set AES256-SHA256-T esp-aes 256 esp-sha256-hmac 
 mode transport require
crypto ipsec transform-set GCM256-T esp-gcm 256 
 mode transport require
crypto ipsec transform-set AES256-SHA512-T esp-aes 256 esp-sha512-hmac 
 mode transport require

banner exec ^C
_____________________________________________________________________
|                                                                   |
|   Model: <Cisco Nexus>                                            |
|    Name: < {{ hostname }}>                                        |
|    Site: Melbourne                                                |
|      SN: < {{ SERIAL }}>                                          |
|Property: GNS                                                      |
|___________________________________________________________________|
^C
banner login ^C

"""
#parameters act as dictionary
parameters = {
    "hostname": hostname,
    "VLAN_IP": vlan_ip,
    "VLAN_IP_MASK": mask,
    "External_IP": external,
    "Internal_IP": internal,
    "SERIAL": serial,
}

#we can take each value of key from dictionary "parameters"
filename = parameters.get("hostname")

result = confgen.render_from_string(
    template_content=template, 
    parameters=parameters
)
if not result.render_error:
	sys.stdout = open(filename + ".txt", "w") #stdout is used to display output directly to the screen console, but with open(file, w - write mode)
	print(result.template_result) #it prints whole output of result = confgen.render_from_string
else: 
    print("Something went wrong: %s" % result.error_text)