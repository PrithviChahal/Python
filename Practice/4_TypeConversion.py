# Take a number as input , convert it to a float , and print both the original and converted values with their data types.


Num = input("Enter the number:")
Datatype_of_Num = type(Num)


Num_to_float = float(Num)
Datatype_of_Num2 = type(Num_to_float)

print(f"Entered Number is {Num} and its datatype is {Datatype_of_Num}")

print(f"Floated Number is {Num_to_float} and its datatype is {Datatype_of_Num2}")



#  swap the values 

a = 10 
b = 5

c = a
a = b
b = c 

print(c)
print(a)
print(b)


# Conversion


aStr = "123456"

print(f"String : {aStr}")
strtoset = set(aStr)
print(f"From string {aStr} to set : {strtoset}")

settolist = list(strtoset)
print(f"From set {strtoset} to list : {settolist}")

print("Before Sorting")

print(settolist)

print("After sorting")

settolist.sort()
print(settolist)

listtostring = "".join(settolist)
print(listtostring)




abc = list("abcdefgh")
print(abc)

abc[0],abc[len(abc)-1] = abc[len(abc)-1],abc[0]
print(abc)



