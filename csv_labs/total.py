import csv
total = 0.0 #wartosc poczatkowa

with open ('/Users/USZCZRA/Python/lab/csv_labs/Routers.csv') as f:
    
   rows = csv.reader (f) # wczytaj wiersze z pliku f
  
   headers = next (rows) #pomin wiersz z naglowkiem

   for row in rows: 

      row [4] = row [4].strip ('$') # z kolumny Unit_price usun znak dolara zeby moc policzyc liczby

      row [4] = float(row [4]) #z kolumy 5tej Unit_price wez wartosc przecinkowa

      row [3] = int(row [3]) #z kolumny 4tej No_of_routers wez liczbe calkowita

      total += row[3] * row[4] #zwieksz wartosc total o iloczyn kolumny 4tej (ilosc routerow) z wartoscia kolumny 5 (cena jednej sztuki)

print('Total cost: $', total)