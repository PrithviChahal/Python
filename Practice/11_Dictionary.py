# Dictionary are unordered
# It is mutable
# dont allow duplicate keys 
# Indexing is not allowed but we have use keys to know the value 


student = {
    "name" : "Prithvi",
    "age" : 20,


}


print(type(student))
print(student)
print(student["age"])

student["name"] = "Pankaj"
print(student)

student["city"] = "Faridabad"
print(student)

print(student.keys())

print(student.items())

a = ["a","b","c"]

b = dict.fromkeys(a,1)

print(b)