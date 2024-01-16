import os

file=('/Users/USZCZRA/Python/lab/csv_labs/Countries.csv')

if os.path.isfile(file): # czy plik istnieje
    print ('Existing')
else:
    print ("Not Existing")
    
print(os.path.abspath(file)) # podaj sciezke pliku
print(os.path.basename(file)) # podaj nazwe pliku
print(os.path.dirname(file)) # podaj tylko sciezk do pliku
print(os.path.exists(file)) # czy ścieka do pliku istnieje

print(os.listdir('/Users/USZCZRA/Python/lab/csv_labs')) #wyswietlanie zawartosci folderu
directory=os.listdir('/Users/USZCZRA/Python/lab/csv_labs') #definicja folderu
plik=os.path.basename(file) #pobranie nazwy pliku
if plik in directory: #sprawdzenie czy plik istnieje juz w folderze
    print("Already existing")
else:
    print("Saved file")
    
