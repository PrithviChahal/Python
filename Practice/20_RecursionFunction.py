#  recursive function 

def abc(num):
     if num !=1:
          return num** abc(num-1)
     else:
          return 1
     


abc(4)


#  recursive function to calculate the sum of digits of a number.


def sum(num):
     
    if num == 0 :
          return 0
     
    return num%10 + sum(num//10)


sum(12345)