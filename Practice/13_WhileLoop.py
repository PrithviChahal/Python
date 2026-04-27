# Print the name 100 times 

num = 0

while num<= 99:
    
    num+=1
    print(f" Index no :{num} , Prithvi chahal")


# Print numbers from 1 to 10 using while loop

no = 1

while no<=10:
    print(no)
    no+=1

# Print numbers from 10 to 1 using while loop 

no2 = 10

while no2>=1:
    print(no2)
    no2-=1


# Print even numbers between 1 to 50 from while loop

a = 1

while a<= 50:
    if a%2 == 0:
        print(f"{a} is even number ")        
    a+=1    

# Print the sum of first natural number using while loop

n = int(input("Enter any number : "))

z = 0

sum = 0

while z<=n :
    sum+=z
    z+=1
    
print(f"Total of number is {sum}")    


#  write a program to print the pattern

num = 1

while num<5:
    print("*" * num)
    num+=1

# Print any name 5 times with the number in front of it  

name = input("Enter your name : ")

num2 = 1

while num2<=5:
    print(f" {num2}. {name}")
    num2+=1



# Print the multiplication table of any number using while loop

TableNo = int(input(" Enter any number of you want table : "))


b = 1

while b<=10:
    print(f" {TableNo} x {b} = {TableNo*b}")
    b+=1