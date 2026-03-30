# Take a number as input , convert it to a float , and print both the original and converted values with their data types.


Num = input("Enter the number:")
Datatype_of_Num = type(Num)


Num_to_float = float(Num)
Datatype_of_Num2 = type(Num_to_float)

print(f"Entered Number is {Num} and its datatype is {Datatype_of_Num}")

print(f"Floated Number is {Num_to_float} and its datatype is {Datatype_of_Num2}")



