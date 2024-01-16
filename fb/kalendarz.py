from calendar import*
import datetime

year = int(input("Podaj rok kalendarzowy: "))
print(calendar(year, 2, 1, 8, 6))
#2 - 2 characters for days (Mo, Tu) ; if 3 - Mon Tue
#1 - 1 lin for each week
#8 - 8 rows for each month
#6 - 6 colums for all months of the year

now = datetime.datetime.now()
print(f"Today is {now:%B %d, %y}")
#f-string - formatting string 
#Every f-string statement consists of two parts, one is character f or F, 
#and the next one is a string which we want to format. The string will be enclosed in single, double, or triple quotes.
#The variables in the curly { } braces are displayed in the output as a normal print statement. Czyli string poza nawiazem {}

# %B - November %b - Nov / %%m - 11
# %d - 13 %D - 11/13/23 
# %Y - 2023 %y - 23