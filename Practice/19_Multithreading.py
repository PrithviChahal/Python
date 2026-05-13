from time import perf_counter , sleep
import threading


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



#  Multithreading

# this takes 3 seconds 

start_time4 = perf_counter()
t1 = threading.Thread(target= hello)
t1.start()
t1.join()
t2 = threading.Thread(target= hello)
t2.start()
t2.join()
t3 = threading.Thread(target = hello)
t3.start()
t3.join()
end_time4 = perf_counter()
total_time4 = end_time4 - start_time4

print(f"Total time taken for hello function is {total_time4}")


#  this takes 1 second

start_time5 = perf_counter()
t1 = threading.Thread(target= hello)
t2 = threading.Thread(target= hello)
t3 = threading.Thread(target = hello)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
end_time5 = perf_counter()
total_time5 = end_time5 - start_time5

print(f"Total time taken for hello function is {total_time5}")


















