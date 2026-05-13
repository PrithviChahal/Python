#  function to print name and age together

def show_age(name = "Prithvi", age = 24):
    print(f"{name} is {age} years old")


show_age("Pankaj",25)
show_age()    


# function that prints both sum and difference of two numbers


def SumAndMinus(num1,num2):
    sum = num1+num2
    minus = num1 - num2

    print(f"Sum of {num1} and {num2} is {sum}")

    print(f"Difference of {num1} and {num2} is {minus}")



#  Function that returns the sqaure of number 

def square(num):
    return num * num


a = square(5)
print(a)


#  function that takes a string and returns the count of vowels and consonants separately


def abc(name):

    vowels = "aeiouAEIOU"

    vowelCount = 0 

    consonantsCount = 0

    for i in name:
        if(i.isalpha()):
            if(i in vowels):
                vowelCount+=1
            else:
                consonantsCount+=1

    return vowelCount , consonantsCount


a , b = abc("prithvi")
print(f"Vowels -> {a}")
print(f"Consonant -> {b}")


#  Function that returns fullname with the space between first and last name 


def fullname(firstname, lastname):
    print(f"Fullname is {firstname} {lastname}")


fullname("Prithvi","singh")    



def hello():
    return "hello"


print(hello())


# local variable and global variable

a = 20 

def local():
    a = 10
    print(a)


def change():
    global a
    a = 30 
    print(a)



local()

change()

print(a)


# Decorator function

def deco(fn):

    def wrapper(a,b):
        print("***********")
        fn(a,b)
        print("***********")

    return wrapper

@deco
def multiplication(a,b):
    print(f"Multiplication of {a} and {b} is {a*b}")

multiplication(5,5)    



#  closure 


def abc(num):
    return lambda a:a*num


a = abc(10)
a(10)


#  prime number 

def prime():
    n = int(input(f" Enter any number : "))

    if n%n == 0 and n%1==0:
        print(f" {n} is prime number")
    else:
        print(f" {n} is not a prime number ")   


