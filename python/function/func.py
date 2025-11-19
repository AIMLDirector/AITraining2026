# def firstfun():
#     print("This is the first function.")

# firstfun()

# def add(a:int=20,b:int=30):
#     sum = a + b
#     print(sum)
#     print("first function invoke :")
#     return sum,a,b 

# add(5,10) 
# add(20,30)
# add(100,200)
# add()
# v1,v2,v3 = add()
# print(v1,v2,v3)


def add(a,b):
    sum = a + b
    return sum

# output = add(5,10)
# print(output)

# age validation function
def age_validation(age:int = 18):
    if age < 18:
        return "You are not eligible to vote."
    else:
        return "You are eligible to vote."

result = age_validation(20)
print(result)
result1 = age_validation()
print("result1:", result1)



   