
name = ["kumar", "ravi", "sachin"]

# for i in name:
#     print(i)

for i in name:
    if i == "ravi":
        print(f"Hello, {i}!")

for i in name:
    if i.startswith("s"):
        continue
    print(f"Hi, {i}!")

# dirpath = input("Enter directory path:")
# if os.chdir(dirpath):
#     print(f"Changed directory to: {dirpath}")
#     for i in dirpath:
#         if i.endswith(".txt"):
#             print(f"Text file found: {i}")
# else:
#     print("Invalid directory path.")

for i in range(5):
   if i == 3:
        break
   print(i)
   

