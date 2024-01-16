#import time
#print(dir (time))

def silnia(n):
    if n == 1:
        return 1
    else:
        return n * silnia(n-1)
    
result = silnia(6)
print (result)
print (int(36 ** 0.5))

a = [1,2,3]
b = a
a = [4,5,6]

print (b)

def say_hello(name='Karpiu'):
    print('Hello ' + name)
    
say_hello('Radek')
say_hello()

dialing_code = {'England': '+44', 'Greece': '+30', 'Italy': '+39', 'Spain': '+34', 'France': '+33'}

for country, code in dialing_code.items() :
    print('The country code for ' + country + ' is ' + code)
    
lam = [lambda x,y:x+y, lambda x,y:x-y, lambda x,y:x*y, lambda x,y:x/y]
print(lam[0](3,2))
print(lam[1](3,2))
print(lam[2](3,2))
print(lam[3](3,2))
