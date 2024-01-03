import csv

f = open('/Users/USZCZRA/Python/lab/csv_labs/NaaS_Remove.csv', 'r', encoding="utf8", errors='ignore')
kosztorys = open('/Users/USZCZRA/Python/lab/csv_labs/Select.csv', 'w+', newline='')
zapis = csv.writer (kosztorys, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
for line in f:
    x=line.split(';')[0] #drukuj pierwsza kolumne [0], ktora odrozniana jest ";"
    y=line.split(';')[1]
    z=line.split(';')[4]
    print(x, y, z)
    zapis.writerow([x,y,z]) #zapisz wybrane kolumny do nowego pliku

kosztorys.close()
f.close()