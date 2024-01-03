import re  

sw_mac = '''pynetauto-sw01 84:3d:c6:05:09:11
... pynetauto-sw17 80:7f:f8:80:71:1b
... pynetauto-sw05 f0:62:81:5a:53:cd'''

sw_mac = sw_mac.replace(":", "").upper()

#print (sw_mac)
#PYNETAUTO-SW01 843DC6050911
#... PYNETAUTO-SW17 807FF880711B
#... PYNETAUTO-SW05 F062815A53CD

list1 = sw_mac.split(" ")

#print(list1) 
#['PYNETAUTO-SW01', '843DC6050911\n...', 'PYNETAUTO-SW17', '807FF880711B\n...', 'PYNETAUTO-SW05', 'F062815A53CD']

list2 = []         
for i in list1:          
    list2.append(i.strip('\n...')) 
    
#print(list2)
#['PYNETAUTO-SW01', '843DC6050911', 'PYNETAUTO-SW17', '807FF880711B', 'PYNETAUTO-SW05', 'F062815A53CD']

sw_list = []         
mac_list = []        
for i in list2:      
    if len(i) == 14: 
        sw_list.append(i)     
    if len(i) == 12:          
        i = i[:6] + "******"  
        mac_list.append(i)
        
#print(sw_list)
#print(mac_list)
#['PYNETAUTO-SW01', 'PYNETAUTO-SW17', 'PYNETAUTO-SW05']
#['843DC6******', '807FF8******', 'F06281******']

sw_mac_dict = dict(zip(sw_list, mac_list))    

#print(sw_mac_dict)
#{'PYNETAUTO-SW01': '843DC6******', 'PYNETAUTO-SW17': '807FF8******', 'PYNETAUTO-SW05': 'F06281******'}

print("Without regex: ")

for k,v in sw_mac_dict.items():         
    print(k, v, end='\n')
    
#PYNETAUTO-SW01 843DC6******
#PYNETAUTO-SW17 807FF8******
#PYNETAUTO-SW05 F06281******

print()
print('With regex:')
         
sw_mac_regex = sw_mac.replace(":", "").upper() 
sw_mac_regex = sw_mac_regex.replace("... ", "")     
pattern = re.compile("([0-9A-F]{6})" "([0-9A-F]{6})")   
print(pattern.sub("\g<1>******", sw_mac_regex))          