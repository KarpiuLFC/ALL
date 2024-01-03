import re
expr = 'I was born in 2,009 and I am 15 years old. I started my primary school in 2,010'
p = re.compile(r"""
[1-9]           # Match a single digit between 1-9
(?:\d{0,2})     # Match digit equalt to [0-9] (\d) between 0 and 2 times ({0,2})
(?:,\d{3})*     # Dopasuj znak (przecinek)(,), dopasuj cyfrę równą [0-9](\d) \dokładnie 3 razy(3)) Zero lub nieograniczona liczba razy (*)
(?:\.\d*[1-9])? # Dopasuj (Kropka) dosłownie, dopasuj cyfrę równą [0-9] \zero i nieograniczoną liczbę razy (*), dopasuj pojedynczą cyfrę od [1-9]) \zero lub jeden raz (?).
|               # OR
0?\.\d*[1-9]    # Dopasuj 0 zero lub jeden raz(?), dopasuj . (Kropka) dosłownie, dopasuj cyfrę \równą [0-9] zero lub nieograniczoną liczbę razy (*) i dopasuj cyfrę z zakresu [1-9]
|               # OR
0               # Match one 0
""", re.VERBOSE)
m = p.findall(expr)
print(m)

#['2,009', '15', '2,010']