file = open('spf_update.csv', 'r+', encoding='UTF8', errors='ignore') # open csv file with only one TAB, .csv file with utf-8 encoding and seprated with ";" 

action = input(str("Provide an action: ")) # ask for action type, however this script is dedicated for update action
record = input(str("Provide an record_type: ")) # ask for record type 
view = input(str("Provide a view: ")) # ask for common 
index=0

final = open('spf_update.yaml', 'w+', newline='') # open a final .yaml file with our output

for line in file.readlines(): # read all lines in csv file
    current = str(line.split(';')[3]) # take 4 column (current TXT value)
    new = str(line.split(';')[5]) # take 6 column (new TXT value)
    name = str(line.split(';')[2]) 
    print("#" + str(index))
    print("- action: "+ action)
    print("  record_type: " + record)
    print("  record_name: " + name.strip())
    print("  text: " + current)
    print("  view: " + view)
    print("  new_record_name: " + name.strip())
    print("  new_text: " + new.strip())
    print()
    final.write("# "+ str(index) + "\n")
    final.write("- action: "+ action + "\n")
    final.write("  record_type: " + record + "\n")
    final.write("  record_name: " + name.strip() + "\n")
    final.write("  text: " + current + "\n")
    final.write("  view: " + view + "\n")
    final.write("  new_record_name: " + name.strip() + "\n")
    final.write("  new_text: " + new.strip() + "\n")
    final.write("\n")
    index += 1
file.close()
final.close()



    
    
