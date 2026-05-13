# sets is unordered
# indexing is not allowed
# sets remove the duplicate elements 
# it is mutable

Languages = {"Python", "python", "python", "java", "javascript"}

print(Languages)
print(type(Languages))


# create empty set with the help of set()

empty = set()
print(type(empty))


#  sets methods 


a = {1,2,3,4,5,33,21}
b = {2,4,5,16,34}

print(a.difference(b))

print(a)

print(a.difference_update(b))

print(a)


c = {10,20,30,40,50,60}

d = {20,40,50,33,21,56}

print(c.intersection(d))  

print(c.symmetric_difference(d))

print(c.union(d))
