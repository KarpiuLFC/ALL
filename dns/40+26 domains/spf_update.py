#import yaml
import csv

file = open('spf_update.csv', 'r+', encoding='UTF8', errors='ignore')

action = input(str("Provide an action: "))
record = input(str("Provide an record_type: "))
#txt = input(str("Provide a text: "))
view = input(str("Provide a view: "))


final = open('spf_update.yaml', 'w+', newline='')

for line in file.readlines():
    current = str(line.split(';')[3])
    new = str(line.split(';')[5])
    name = str(line.split(';')[2])
    
    print("- action: "+ action)
    print("  record_type: " + record)
    print("  record_name: " + name.strip())
    print("  text: " + current)
    print("  view: " + view)
    print("  new_record_name: " + name.strip())
    print("  new_text: " + new.strip())
    print()
    final.write("- action: "+ action + "\n")
    final.write("  record_type: " + record + "\n")
    final.write("  record_name: " + name.strip() + "\n")
    final.write("  text: " + current + "\n")
    final.write("  view: " + view + "\n")
    final.write("  new_record_name: " + name.strip() + "\n")
    final.write("  new_text: " + new.strip() + "\n")
    final.write("\n")
file.close()
final.close()



    
    
