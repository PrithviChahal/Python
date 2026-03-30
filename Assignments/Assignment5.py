# Program that takes a user name as input and prints :
# the first character 
# the last character 
# total length of name 


Name = input("Enter your name:")

name_length = len(Name)

print(f"First character of your name is : {Name[0]}")

print(f"Last character of your name is : {Name[-1]}")

print(f"Length of your name is: {name_length}")


# Program that takes your favourite food as input and prints middle 3 and last 2 character

favourite_food = input("Enter your favourite food:")

mid = len(favourite_food)//2

print(favourite_food[mid-1:mid+1])

print(favourite_food[-2:])

