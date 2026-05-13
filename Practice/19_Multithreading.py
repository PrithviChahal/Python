from time import perf_counter , sleep


#  Method 1 to find factorial

def factorial(num):
         

        ffactorial = 1
        list1 = [] 

        for i in range(num,0,-1):
            ffactorial*=i
            list1.append(i)
        
        print(f"Factorial of {num} is : " , end="")
        print(*list1 , sep=" x " , end = f" = {ffactorial}\n")



# Method 2 to find factorial with recursion 


def factorial2(num):
      
    if num == 1:
        return 1 
      
    return num * factorial2(num-1)


#  measure the time of function 


start_time = perf_counter()
factorial(9)
end_time = perf_counter()
total_time = end_time - start_time

print(f"Total time taken for factorial function is {total_time}")


start_time2 = perf_counter()
print(factorial2(9))
end_time2 = perf_counter()
total_time2 = end_time2 - start_time2

print(f"Total time taken for factorial2 function is {total_time2}")


#  use of sleep


def hello():
     print("Hello")
     sleep(1)
     print("hii")


start_time3 = perf_counter()
hello()
end_time3 = perf_counter()
total_time3 = end_time3 - start_time3

print(f"Total time taken for hello function is {total_time2}")













