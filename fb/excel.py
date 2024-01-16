import csv

new = open('/Users/USZCZRA/Python/lab/csv_labs/Countries.csv', 'w+', encoding='UTF8')

header = ['country', 'continent', 'country_code', 'capitol']
data = [
    ['Afghanistan', 'Asia', 'AFG', 'Kabul'],
    ['Albania', 'Europe', 'ALB', 'Tirana'],
    ['Algeria', 'Africa', 'DZA', 'Algier'],
    ['Andorra', 'Europe', 'AND', 'Andorra'],
    ['Angola', 'Africa', 'AGO', 'Luanda']
        ]
writer = csv.writer(new)    
    # write the header
writer.writerow(header)
    # write the data
writer.writerows(data)

new.close()

