

# class bankaccount():
#     def __init__(self,name,amount,pin):
#         self.name = name
#         self.amount = amount
#         self.pin = pin

#     def deposit(self):
#         self.depositAmount = int(input("Enter the amount for deposit : "))
#         self.askpin = int(input("Enter the PIN of your account to deposit the amount : "))

#         if self.askpin == self.pin:
#             self.amount+= self.depositAmount
#             print("Deposit successfully")
#         else:
#             print("Please enter valid pin")

#     def withdraw(self):
#         self.withdraww = int(input("Enter the amount you want to withdraw : "))
#         self.askpin2 = int(input("Enter the PIN for withdraw : "))

#         if self.amount >= self.withdraww:
#             if self.askpin2 == self.pin:
#                 self.amount-=self.withdraww
#                 print("Amount withdraw successfully")
#             else:
#                 print("Please enter valid PIN")
#         else:
#             print("You don't have that much money.")

#     def checkBalance(self):
#         self.askpin3 = int(input("Enter the PIN to check the balance : "))

#         if self.askpin3 == self.pin:
#             print(f"You have only amount : {self.amount}")
#         else:
#             print("Please enter valid PIN")

#     def changePin(self):
#         self.askpin4 = int(input("Enter your old PIN : "))

#         if self.askpin4 == self.pin:
#             self.updatedPin = int(input("Enter your new PIN : "))

#             self.pin = self.updatedPin
#             print("PIN changed successfully...")

#         else:
#             print("Please Enter valid PIN")    

                         


# ab = bankaccount("Prithvi",10000,2001)


# ab.withdraw()
# ab.checkBalance()
# ab.deposit()
# ab.checkBalance()
# ab.changePin()
# print(ab.pin)
                         


class series():
    def __init__(self):
        pass

    def fabonnaci(self):
        self.num1 = int(input(f"Enter first number : "))
        self.num2 = int(input(f"Enter second number : "))
        self.Length = int(input(f"Enter the length you want : "))
        self.a = []
        self.a.append(self.num1)
        self.a.append(self.num2)

        for i in range(self.num1,self.Length-1):
            self.num3 = self.num1+self.num2
            self.a.append(self.num3)
            self.num1 =self.num2
            self.num2 = self.num3
        print(self.a)


    def armstrong(self):
        self.n = int(input("Enter any number : "))

        self.total = 0
        self.astr = str(self.n)
        self.power = len(self.astr)

        for i in self.astr:
            self.x = int(i)
            self.z = self.x**self.power
            self.total+= self.z 

        if self.total == self.n :
            print(f"{self.n} is a armstrong number")
        else:
            print(f"{self.n} is not a armstrong number") 


    def factorial(self):
        self.n2 = int(input("Enter the number you want factorial of : "))

        self.ffactorial = 1
        self.list1 = [] 

        for i in range(self.n2,0,-1):
            self.ffactorial*=i
            self.list1.append(i)
        
        print(f"Factorial of {self.n2} is : " , end="")
        print(*self.list1 , sep=" x " , end = f" = {self.ffactorial}")



    def perfect(self):
        self.n3 = int(input("Enter any number : "))

        self.z = 0

        for i in range(1,self.n3):
            if self.n3%i ==0:
                self.z+=i
            else:
                pass

        if self.z == self.n3:
            print(f"{self.n3} is a perfect number")
        else:
            print(f"{self.n3} is not a perfect number")  



    def prime(self):
        self.number = int(input("Enter any number : "))

        self.factor = 0

        for i in range(1,self.number+1):
            if self.number%i==0:
                self.factor+=1

        if self.factor == 2:
            print(f"{self.number} is a prime number")
        else:
            print(f"{self.number} is not a prime number")            








a = series()

a.prime()

