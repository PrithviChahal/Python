#  Print a countdown before something exciting happens like happy new year , birthdaywish etc ....

import time 


Counter = int(input("Enter any Counter number : "))

print("Countdown starts now ")

for i in range (Counter, 0, -1):
    print(i)
    time.sleep(1)

print(" Happy new year ")