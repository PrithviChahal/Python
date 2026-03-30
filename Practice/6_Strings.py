# Strings are immutable

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