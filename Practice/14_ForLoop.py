# Program to write all even numbers between 1 and 20 usinf for loop


for i in range(1,21):
    if i%2 == 0:
        print(i)


#  program to write 1 to 10 but skips 7


for i in range(1,11):
    if i == 7:
        continue
    print(i)