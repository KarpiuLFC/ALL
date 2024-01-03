import re
expr = " . ^ $ * + ? \ | ( ) [ ] { }" 
# Indeks w stringu:0 - spacja, 1- . 2 spacja 3- ^ 4- spacja 5- $ 6- spacja 7- * 8- spacja 9- + 10- spacja 11- ? 12- spaja 13- \  
# 14- spacja, 15- | 16 spacja 17- () 18- spacja 19- ) 20- spacja 21- [ 22- spacja 23- ] 24- spacja 25- { 26- spaja 27- } 
a = re.search(r'[\^]', expr) 
#######################################################
print(a)
# <re.Match object; span=(3, 4), match='^'> - symbol ^ znajduje sie jako 3ci znak w stringu expr
b = re.search(r'[\\]', expr)
# <re.Match object; span=(13, 14), match='\\'> - symbol \ znajduje sie jako 13ty znak w stringu expr
print(b)
#######################################################
c = re.findall('[^a]', 'abracadabra') # znajdz wszystkie NIE-a

print(c)
# ['b', 'r', 'c', 'd', 'b', 'r']
#######################################################
d = re.search(r'[\\]', 'match \ or ]') # Indeks w stringu: 0- m 1- a 2- t 3- c 4- h 5- spacja 6- \ 7 -spacja 8- o 9- r 10- spacja 11- ] 12- spacja

print(d)
# <re.Match object; span=(6, 7), match='\\'> - symbol \ znajduje sie jako 6ty znak w stringu 'match \ or ] '
#######################################################
e = re.search(r'[\]]', 'match \ or ]')

print(e)
# <re.Match object; span=(11, 12), match='\\'> - symbol ] znajduje sie jako 11ty znak w stringu 'match \ or ] '

f = re.findall('\dx\d{4}', "Configuration register is 0x2102") # znajdz cyfre, litere x i kolejne 4 cyfry
#######################################################

print(f)
# ['0x2102']
#######################################################
expr1 = 'automation' #<re.Match object; span=(0, 10), match='automation'>
expr2 = 'Automation' #None
expr3 = 'AUTOMATION' #None
p = re.compile('[a-z]+') 
m1 = p.match(expr1)
print(m1)
#######################################################
sentence = 'Our team \scored three goals\\'
p2 = re.compile(r'\\scored') # r - raw = wiersz, bez tego r nie znajdzie \\scored
g = p2.findall(sentence)
print(g)
#['\\scored']

h = g[0] # -bez nawiasow 
print('h= ', h)
#\scored

for i in h:
     print(i, end='')

print()
#\scored%
#######################################################

j = re.findall('^S.+sh$', 'Start to finish') # dzieki kombinacji ^ - start string i 
print(j)
#['Start to finish']

k = re.findall('^S.+sh$', '''Start to finish
               \nSpecial fish
               \nSuper fresh''', re.MULTILINE)
print(k)
['Start to finish', 'Special fish', 'Super fresh']
#######################################################

text = '''SYDCBDPIT-ST01#sh ip int brief
... Interface              IP-Address      OK? Method Status                Protocol
... Vlan1                  unassigned      YES NVRAM  up                    up
... Vlan50                 10.50.50.11     YES NVRAM  up                    up
... FastEthernet0          unassigned      YES NVRAM  down                  down
... GigabitEthernet1/0/1   unassigned      YES unset  down                  down
... GigabitEthernet1/0/2   unassigned      YES unset  up                    up
... GigabitEthernet1/0/3   unassigned      YES unset  up                    up
... '''
hip = re.compile('^... Gi.+down$', re.MULTILINE)
l = hip.findall(text)
print(l)
#['... GigabitEthernet1/0/1   unassigned      YES unset  down                  down']
#######################################################

m = re.findall('\AS.+sh', '''Start to finish
                         \nSuper special fish
                         \nSuper fresh fish
                         \nSuper smelly fish''', re.M)
print(m)
#['Start to finish']

n = re.findall('S.+sh\Z', '''Start to finish
                         \nSuper special fish
                         \nSuper fresh fish
                         \nSuper smelly fish''', re.M)
print(n)
#['Super smelly fish']
#######################################################

grupowanie = "Did you know that that 'that', that that that person used in that sentence, is wrong."
szukaj = re.compile(r'(\bthat)\s+\1') # \b - po odstepie "that", \s - spacja, znak + oznacza dopasowanie tych samych ciągów znaków, 
#co poprzednia grupa - czyli jeszcze jedno "that" 
#a \1 oznacza ponowne odniesienie do grupy nr 1. Jeśli istnieje druga grupa i chcesz się do niej odwołać, można użyć \2.
o = szukaj.search(grupowanie)
print("o = " ,o)
#o =  <re.Match object; span=(13, 22), match='that that'>
p = szukaj.search(grupowanie).group()
print("p = " ,p)
# =  that that - pierwsze podwojne that that w stringu
#######################################################

texxxt = "SYD-GW1 uptime is 1 year, 9 weeks, 2 days, 5 hours, 26 minutes"
group_named = re.compile(r'(?P<hostname>\w+[-]\w+)\s.+(?P<uptime>(?P<years>\d+\sy\w+),\s(?P<weeks>\d+\sw\w+),\s(?P<days>\d+\sd\w+),\s(?P<hours>\d+\sh\w+),\s(?P<minutes>\d+\sm\w+))')
r = group_named.search(texxxt)
print("Minutes: ", r.group("minutes"))
#Minutes:  26 minutes
print("Uptime: ", r.group("uptime"))
#Uptime:  1 year, 9 weeks, 2 days, 5 hours, 26 minutes
print("Hostname: ", r.group("hostname"))
#Hostname:  SYD-GW1

number = "+1 408 526 1234"

noncaptruring = re.compile(r"((?:(\+1)[ -])?\(?(\d{3})\)?[ -]?\d{3}[ -]?\d{4})")
#((?:(\+1)[ -])?\(?(\d{3})\)?[ -]?\d{3}[ -]?\d{4}) - grupa (0), (?:(\+1)[ -]) - grupa (1), (\+1) - grupa (2), (?(\d{3})\) - grupa (3)
#
s = noncaptruring.search(number)

print(s)
#<re.Match object; span=(0, 15), match='+1 408 526 1234'>

print(s.group(2))
#+1

wiecej = "vlan.dat\nsw1.bak\nconfig.text\npynetauto.dat\nsw1_old.bak\n2960x-universalk9-mz.152-2.E6.bin"
t = re.findall(".*[.].*$", wiecej, re.M) # . - wszystkie znaki * - zero lub wiecej (poprzedni znak), [.] - kropka, . - wszystkie znaki * - zero lub wiecej (poprzedni znak)
print(t)
#['vlan.dat', 'sw1.bak', 'config.text', 'pynetauto.dat', 'sw1_old.bak', '2960x-universalk9-mz.152-2.E6.bin']

ip = '172.168.123.245'
print ('.'.join([bin(int(x)+256)[3:] for x in ip.split('.')]))