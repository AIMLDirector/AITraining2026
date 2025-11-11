# d1 = {"name" : "kumar", "Address": "HSR", "working" : "AI" }
# print(d1)
# print(d1["name","working"])
# print("keys in the dictionary:")
# print(d1.keys())
# print("values in the dictionary:")
# print(d1.values())
# print("Both key and value in the dictionary:")
# print(d1.items())

student = {}
student1 = {}
num_of_students = int(input("Enter number of students: "))
for i in range(num_of_students):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    college = input("Enter student college: ")
    student[name] = {"age": age, "college": college}
  


print("Student Details:")
for name, details in student.items():
    print(f"Name: {name}, Age: {details['age']}, College: {details['college']}")

print(student)

    