import os
import sys
import csv
import yaml
import re
import pandas as pd
import warnings

warnings.simplefilter(action='ignore', category=UserWarning) #to avoid warning like below: 
#python3.11/site-packages/openpyxl/worksheet/_reader.py:329: UserWarning: Data Validation extension is not supported and will be removed warn(msg)

def open_xlsx():
    global source
    source = os.path.expanduser(sys.argv[1]) #define source of file - need to be specify as atribute of python - python multi.py /Users/USZCZRA/Desktop/INC0264729.csv
    read_file = pd.read_excel (source) # Write the dataframe object 
    global without_extension
    without_extension = os.path.splitext(source)[0]
    read_file.to_csv (f"convert_{without_extension}.csv", index = None, header=True) #into csv file 
open_xlsx()
d = {} # empty dictionary
output = {'records': []} #define empty dictionary that would be updated with data yaml structure
index=0 #start counting of generated records based on a number of rows

update = re.compile('[uU][pP][dD][aA][tT][eE]')

with open(f"convert_{without_extension}.csv", newline='', encoding="utf-8-sig") as file:
    csv.reader = csv.DictReader(file, delimiter=',', quotechar='"')
    separator = csv.reader# read row as a list
    template = [row for row in separator]
    for row in template:
        d.update(row)
        data = { #structure of yaml dictionary
            "record_type" : d.get("record_type"), #create key "record type" and match value (lower case) from the column type
            "action" : d.get("action"), #create key "action" and match value (lower case) from the column action
            "record_name" : d.get("record_name"), #create key "record name" and match value (lower case) from the column record
            "view" : d.get("view"), #create key "view" and match value (lower case) from the column view
                }
        
        for value in d.values():
            if not d.get('record_type', '').lower(): # equals the same as: if not d.get('Record Type', '').lower():
                print("Record Type is missing for " + str(d.get("record_name")))
                exit()
            #if d.get("action") is None: None doesnt work
            if not d.get('action', '').lower():
                print("Action is missing for " + str(d.get("record_name")))
                exit()
            if not d.get('record_name', '').lower():
                print("Record Name is missing for line " + str(index+1))
                exit()
            if not d.get('view', '').lower():
                print("View is missing for " + str(d.get("record_name")))
                exit()
            match d.get('record_type', '').lower():
                case 'a':
                    # dictionary.get(keyname, value) - value: Optional. A value to return if the specified key does not exist. Default value None
                    if not d.get('value', '').lower():
                        print("IP is missing for " + str(d.get("record_name")))
                        exit()
                    data["ip"] = d.get("value") #add key "text" to data dictionary for TXT record
                    #if d.get('action','').lower() == "update":
                    if update.search(value):
                        if not d.get('new_value', '').lower():
                            print("New IP is missing for " + str(d.get("record_name")))
                            exit()
                        #data['new_record_name'] = dict.get("New_Record_UPDATE") #add key "new record name " to data dictionary for TXT record and update action - 'new_record_name' not needed for update action
                        data['new_ip'] = d.get("new_value") #add key "new text" to data dictionary for TXT record and update action
                    if d.get("action") == "delete":
                        data['delete_all'] = d.get("remove_all_records",'').lower()
                case 'cname':
                    if not d.get('value', '').lower():
                        print("Canonical value is missing for  " + str(d.get("record_name")))
                        exit()
                    data['canonical'] = d.get("value") #add key "canonical" to data dictionary for CNAME record
                    if update.search(value): 
                        data.pop('canonical') #remove key "canonical" to data dictionary for CNAME record and update action
                        if not d.get('new_value', '').lower():
                            print("New Canonical is missing for " + str(d.get("record_name")))
                            exit()
                        data['new_canonical'] = d.get("new_value") #but add key "new canonical" to data dictionary for CNAME record and update action
                case 'txt':
                    if not d.get('value', '').lower():
                        print("IP address as a value is missing for " + str(d.get("record_name")))
                        exit()
                    data['text'] = d.get("value") #add key "ip address" to data dictionary for A record
                    if update.search(value):
                        if not d.get('new_value', '').lower():
                            print("New Text Value is missing for " + str(d.get("record_name")))
                            exit()
                        data['new_text'] = d.get("new_value") #add key "new ip address" to data dictionary for A record and update action
                case 'alias':
                    if not d.get('value', '').lower():
                        print("Target Name as value is missing for " + str(d.get("record_name")))
                        exit()
                    if not d.get('alias_target_type', '').lower():
                        print("Alias Target Type is missing for " + str(d.get("record_name")))
                        exit()
                    data['target_type'] = d.get("alias_target_type") #add key "target type" to data dictionary for Alias record
                    data['target_name'] = d.get("value") #add key "target name" to data dictionary for Alias record
                    if update.search(value):
                        if not d.get('new_value', '').lower():
                            print("New Target Name is missing for " + str(d.get("record_name")))
                            exit()
                        data['new_target_name'] = d.get("new_value") #add key "new text" to data dictionary for TXT record and update action
                case 'host':
                    if not d.get('value', '').lower():
                        print("IP address is missing for " + str(d.get("record_name")))
                        exit()
                    for host in [d.get("value")]:
                        data['ips'] = [d.get("value")] #add key "ip address" to data dictionary for Host record
                        #print(d.get("value"))
                    if update.search(value):
                        if not d.get('new_value', '').lower():
                            print("New IP Address is missing for " + str(d.get("record_name")))
                            exit()
                        data['new_ip_address'] = d.get("new_value") #add key "new ip address" to data dictionary for Host record and update action
                case 'mx':
                    if not d.get('value', '').lower():
                        print("Mail Exchanger as a value is missing for " + str(d.get("record_name")))
                        exit()
                    if not d.get('mx_preference', '').lower():
                        print("MX preferance is missing for " + str(d.get("record_name")))
                        exit()
                    data['preference'] = int(float(d.get("mx_preference"))) #add key "preference" to data dictionary for MX record
                    data['exchanger'] = d.get("value") #add key "mail exchanger" to data dictionary for MX record
                    if update.search(value): 
                        if not d.get('new_value', '').lower():
                            print("New Mail Exchanger is missing for " + str(d.get("record_name")))
                            exit()
                        data.pop('preference') #remove key "preference" to data dictionary for MX record and update action
                        data['new_exchanger'] = d.get("new_value") #add key "new mail exchanger" to data dictionary for MX record and update action
                        data['new_preference'] = d.get("mx_preferance") #add key "new preference" to data dictionary for MX record and update action
                    if d.get("action") == "delete":
                        data['delete_all'] = d.get("remove_all_records",'').lower()
                case 'ptr':
                    #data.pop('record_name') NIE DZIALA USUWANIE "record_name" !!!!!!!
                    data['dname'] = d.get("record_name",'').lower()
                    if not d.get('value', '').lower():
                        print("IP address as a value is missing for " + str(d.get("record_name")))
                        exit()
                    data['ip'] = d.get("value") #add key "ip address" to data dictionary for PTR record
                    if update.search(value): 
                        if not d.get('new_value', '').lower():
                            print("New IP Address is missing for " + str(d.get("record_name")))
                            exit()
                        data['new_dname'] = d.get("new_value",'').lower() #add key "new ip address" to data dictionary for PTR record and update action
                    if d.get("action") == "delete":
                        data['delete_all'] = d.get("remove_all_records",'').lower()
                case all:
                    print("Incorrect Record Type for " + str(d.get("record_name")))
                    exit()
                                   
        output['records'].append(data)
        index += 1  # increase index by 1 with each line

print("Found " + str(index) + " records in request") # Print sum of records 
    
file = input("Please provide name of destination yaml file: ") #+ ".yaml"  # ask for destination file name
if file.endswith('.yaml'): # check if format of file is with .yaml
    convert = file
elif file.endswith('.yml'): # or check if format of file is with .yml
    convert = file
else: # if no extansion 
    convert = str(file) + ".yaml" # add .yaml to name of file
    
with open (convert, 'w+') as final: #open destination file
    yaml.dump(output, final) #write outout in .yaml format       
           
entry = 1    # define start count of DNS records
p = '- action:' # looking for "-action"
with open (convert, 'r', newline='' ) as yamlfile: # open created file
    check = yaml.safe_load_all(yamlfile) # read yaml structure
    for linia in yamlfile.readlines(): # analyze each line
        linia = linia.strip() # read only content without unnecessary characters     
        if p in str(linia):  # if "- action" in linia
            entry += 1 # increase count by 1
    print('Created file ' + convert + ' with ' + str(entry-1) + " DNS records") # have to -1 due to after last DNS entry count has been increased by 1
    
os.remove(f"convert_{without_extension}.csv") 