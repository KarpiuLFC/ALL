from pandas import *

# reading CSV file
data=read_csv('/Users/USZCZRA/Python/lab/csv_labs/company_sales_data.csv')
 
# converting column data to list
month = data['month_number'].tolist()
fc = data['facecream'].tolist()
fw = data['facewash'].tolist()
tp = data['toothpaste'].tolist()
sh = data['shampoo'].tolist()
 
# printing list data
print('Facecream:', fc)
print('Facewash:', fw)
print('Toothpaste:', tp)
print('Shampoo:', sh)