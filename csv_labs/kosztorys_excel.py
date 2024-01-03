import csv

with open ('/Users/USZCZRA/Python/lab/csv_labs/Routers.csv', 'w', newline='' ) as csvfile:
    
    filewriter = csv.writer (csvfile, delimiter = ',', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    filewriter.writerow (['Site', 'Router_Type', 'IOS_Image', 'No_of_routers', 'Unit_price($)', 'Purchase_Date'])
    filewriter.writerow(['NYNY', 'ISR4351/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 4, '$ 9100.00', '1-Mar-20'])
    filewriter.writerow(['LACA', 'ISR4331/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 2, '$ 5162.00', '1-Mar- 20'])
    filewriter.writerow(['LDUK', 'ISR4321/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 1, '$ 2370.00', '3-Apr- 20'])
    filewriter.writerow(['HKCN', 'ISR4331/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 2, '$ 5162.00', '17-Apr-20'])
    filewriter.writerow(['TKJP', 'ISR4351/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 1, '$ 9100.00', '15-May-20'])
    filewriter.writerow(['MHGM', 'ISR4331/K9', 'isr4300-universalk9.16.09.05.SPA.bin', 2, '$ 5162.00', '30-Jun-20'])
        
csvfile.close()

f = open('/Users/USZCZRA/Desktop/Routers.csv', 'r', encoding="utf8", errors='ignore')

for line in f:
    print(line.strip(), end="\n")

f.close()

f = open('/Users/USZCZRA/Desktop/Routers.csv', 'r', encoding="utf8", errors='ignore')
for line in f:
        wiersz= f.read().split('\n') # Definicja wiersza
        #count = len(f.read().split('\n')) #Ilosc otrzymanych wierszy po podzieleniu ich od nowej linii - ilosc wierszy
            
z=wiersz[5] #Wybór wiersza liczac od pierwszego /n

site=z.split(',')[0] # Pierwsza kolumna - Site
price=z.split(',')[4] # Druga kolumna - Unit_price

print (site, price)  

f.close()
        


