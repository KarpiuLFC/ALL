import yaml

file = open('start.txt', 'r+', encoding='UTF8')

act = input(str("Provide an action: "))
record = input(str("Provide an record_type: "))
txt = input(str("Provide a text: "))
zone = input(str("Provide a view: "))



final = open('final.yaml', 'w+', encoding='UTF8')

for line in file.readlines():
    print("- action: "+ act)
    print("  record_type: " + record)
    print("  record_name: " + line.strip())
    print("  text: " + txt)
    print("  view: " + zone)
    print()
    final.write("- action: "+ act + "\n")
    final.write("  record_type: " + record + "\n")
    final.write("  record_name: " + line.strip()+ "\n")
    final.write("  text: " + txt + "\n")
    final.write("  view: " + zone + "\n")
    final.write("\n")
file.close()
final.close()



    
    
