import re


a = "This is a python class , python is case sensitive language"

print(re.findall("[is]",a))

print(re.findall("a-z",a))

print(re.findall("py...n",a))

print(re.findall("p.*n",a))

print(re.findall("p.+n",a))

print(re.findall("p.?n",a))

print(re.findall("^This",a))

print(re.findall("language$",a))

print(re.findall("c.{2}e",a))

print(re.findall("class|hello",a))

print(re.findall(r"\bsens",a))

print(re.findall(r"sens\b",a))

print(re.search("python",a))

print(a[10:16])


print(re.split("is",a))

print(re.sub("python","java",a))


# step to remove second number python from a variable and replace to java  

b = a.split()

print(b)

b[6] = "java"

a = " ".join(b)

print(a)

print(type(a))