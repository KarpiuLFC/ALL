
# importing the module
import csv
 
# open the file in read mode
filename = open('/Users/USZCZRA/Python/lab/csv_labs/company_sales_data.csv', 'r')
 
# creating dictreader object
file = csv.DictReader(filename)
 
# creating empty lists
month = []
totalprofit = []
totalunit = []
 
# iterating over each row and append
# values to empty list
for col in file:
    month.append(col['month_number'])
    totalprofit.append(col['moisturizer'])
    totalunit.append(col['total_units'])
 
# printing lists
print('Month:', month)
print('Moisturizer:', totalprofit)
print('Total Units:', totalunit)

