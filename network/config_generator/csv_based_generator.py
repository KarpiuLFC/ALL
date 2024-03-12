from networkconfgen import NetworkConfGen
import sys
import os
import csv

source = os.path.expanduser(sys.argv[1]) #define source of file - need to be specify as atribute of python - python multi.py /Users/USZCZRA/Desktop/INC0264729.csv
#source = 'dmarc_cname_create.csv'
output = {'records': []} #define empty dictionary that would be updated with data yaml structure
index=0 #start counting of generated records based on a number of rows

with open(source, newline='') as file:
    separator = csv.reader(file, delimiter=';', quotechar='"') # read row as a list
    headers = next(separator) # avoid headers
    for line in separator: #read file line by line 
        (hostname, vlan_ip, mask, external, internal, serial) = line   

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
        default_stdout = sys.stdout # define console as default output terminal
        if not result.render_error:
            print ( "================================= " + filename +  " =================================" )
            print("Creating " + filename + " config")
            sys.stdout = open(filename + ".txt", "w") #stdout is used to display output directly to the screen console, but here with open(file, w - write mode) file
            print(result.template_result) #it prints whole output of result = confgen.render_from_string
            sys.stdout.close()
        else: 
            print("Something went wrong: %s" % result.error_text)
        
        sys.stdout = default_stdout    
        
        path = filename + ".txt"
        if os.path.isfile(path):
            sys.stdout.write("Generated file " + filename + ".txt")
            print()
            print( "======================================================================================" )
            print()
        else:
            sys.stdout.write("Something went wrong for " + filename)
