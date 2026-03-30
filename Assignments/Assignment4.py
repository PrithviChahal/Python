# Program that takes total bill amount and number of friends as input , 
# calculate how much each person will pay ,
# also print the data type of each variable  


Bill_amount = float(input("Enter the bill amount:"))

No_of_friends = int(input("Enter the no of friends:"))

Bill_per_person = Bill_amount/No_of_friends

print(f"Bill per person is: {Bill_per_person}, and type is: {type(Bill_per_person)}")

print(f"Bill amount type: {type(Bill_amount)}")

print(f"Type of No_of_friends: {type(No_of_friends)}")




