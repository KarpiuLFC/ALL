import yaml
import os
import sys

source = os.path.expanduser(sys.argv[1])
#source = 'dmarc_cname_create.csv'
output = {'records': []}
index=0

with open(source, 'r') as file:
    for line in file.readlines():
        line = line.strip()
        (type, action, view, record, value) = line.split(";")
        data = {
            "record_type" : type.lower(),
            "action" : action.lower(),
            "record_name" : record,
            "view" : view.lower()
                }
        if type.lower() == "txt":
            data['text'] = value
        elif type.lower() == "cname":
            data['canonical'] = value
        output['records'].append(data)
        index += 1  

file = input("Please provide name of destination yaml file: ") + ".yaml"        
with open (file, 'w+') as final:
    yaml.dump(output, final)
print("Generated " + str(index-1) + " records")

# Skip head of columns
# Combine regex module to work on .yaml 
# Take a look on update type and add required values
# Add comments
