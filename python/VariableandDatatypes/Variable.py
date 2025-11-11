
# Global variable declaration and static variable type 
# Name_team = 20
# Name1 = "kumar"
# Number1 = 10.5
# print(Name_team)
# # We are Dealing with integer, float and string data types
# #ctrl + / to comment or uncomment multiple lines / command + / in mac
# print(type(Name_team))
# print(type(Name1))
# print(type(Number1))

# # Adding the dynamic input value to the variable
# Name_team = input("Enter the team value:")
# print(Name_team)
# # any variable mentioned inside a function is called local variable
# def f1():
#     print("printing inside the function:", Name_team)
#     Name2 = 40
#     print("printing inside the function for name2:", Name2)

# f1()

# print()
# type()
# input()
# upper()
# lower()
# len()

x = 10
y = 2.5
z = 10j 
print(type(x))
print(type(y))
print(type(z))

a = 'hello world'
b = "hello World324231 20"
print(type(a))
print(type(b))
age = 20
name = "kumar"
print("the value of a is :", a)
print("the value of b is :", b)

# %s - String
# %d - Integer
# %f - Float

print(f"the age of {name} is {age}")  # preferred way
print("the age of %s is %d" %(name, age))
print("the age of {} is {}".format(name, age))

l1 = []  # empty list
l2 = [10,11,12,2.5,3j,"kumar",10,True]   # index and values 
print(l2[0:5])
print(l2[-1])

l3 = [10,40,29,50,6,13]
l3.sort()
print(l3)
l3.reverse()
print(l3)
#Adding and removing elements from the list
l3.append(100)
print(l3)
l3.insert(2,200)
print(l3)
l3.remove(50)
print(l3)
l3.pop()
print(l3)
del l3[2]
print(l3)
l4 = l2 + l3
print(l4)

# append, insert, remove, pop, del, sort, reverse
# clear

l4.clear()
print(l4)  
print(l2)
print(l3)



