import time
a = 10
while a > 0:
    print(a, end="\n")
    time.sleep(1)
    a = a - 1
print(time.strftime("%d %b %H:%M:%S"))  