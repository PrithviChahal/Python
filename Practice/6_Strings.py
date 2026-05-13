# Strings are immutable
# indexing is allowed
# slicing is  allowed
# Modifying is not allowed 

# string concatenation

a = "hello "
b = "world"

c = a + b

print(c)

# length of string

print(len(c))

# Indexing

print(a[4])

#  Slicing

Fruit = "Pineapple"

print(Fruit[-1:-5])

# progarm that takes any word as input and prints 
# the first character
# the last character
# total number of characters 


word = input("Enter any word or sentence:")

print(f"First character of {word} is : {word[0:1]}")
print(f"Last character of {word} is : {word[-1]}")
print(f"Total no of character of {word} is : {len(word)}")

a = "This is python class"

a[13:7:-1]

a[-7:-13:-1]

# Program that takes your favourite food as input and prints middle 3 and last 2 character

favourite_food = input("Enter your favourite food:")

mid = len(favourite_food)//2

print(favourite_food[mid-1:mid+1])

print(favourite_food[-2:])
