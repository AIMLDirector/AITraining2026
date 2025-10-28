
# Global variable declaration and static variable type 
Name_team = 20
Name1 = "kumar"
Number1 = 10.5
print(Name_team)
# We are Dealing with integer, float and string data types
#ctrl + / to comment or uncomment multiple lines / command + / in mac
print(type(Name_team))
print(type(Name1))
print(type(Number1))

# Adding the dynamic input value to the variable
Name_team = input("Enter the team value:")
print(Name_team)
# any variable mentioned inside a function is called local variable
def f1():
    print("printing inside the function:", Name_team)
    Name2 = 40
    print("printing inside the function for name2:", Name2)



