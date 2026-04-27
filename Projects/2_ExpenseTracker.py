# Expense Tracker Project  

expenses = []


print("welcome to expense tracker")

while True:
    print("===MENU===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Expense")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))


    if choice == 1:
        date = input("Enter the date on which you expense : ")
        category = input("Enter the category of expense , for ex: food , travel , books , etc... : ")
        description = input("Enter the description about the expense : ")
        amount = float(input("Enter the amount of expense : "))

        expense = {
            "Date" : date,
            "Category" : category,
            "Description" : description,
            "Amount" : amount
        }

        expenses.append(expense)

        print("Expenses added successfully")
    
    elif choice == 2:
        if len(expenses) == 0:
            print("Yet there is no expenses...")

        else:
            print("There is your expenses : ")
            count = 1

            for eachexpense in expenses:
                print(f"Expense no.{count} -> Date : {eachexpense["Date"]} , Category : {eachexpense["Category"]} , Description : {eachexpense["Description"]} , Amount : {eachexpense["Amount"]}")
                count+=1 

    elif choice == 3:
        total = 0
        for eachexpense in expenses:
            total+=eachexpense["Amount"] 
        print(f"Total expenses = {total}")

    elif choice == 4:
        print("Thank you for using the tracker")
        break

    else:
        print("Invalid choice , Please enter valid choice")                  
