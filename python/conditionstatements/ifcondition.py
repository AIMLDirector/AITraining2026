# a = 10
# b = 20

from hdbcli import dbapi
# if a > b:
#     print("a is greater than b")
# elif a == b:
#     print("a is equal to b")
# elif a < b:
#     print("a is less than b")


a = 10 
b = 20
c = 30

# if a > b and a > c:
#     print("a is greater than b and c")
# elif b > a and b >c:
#     print("b is greater than a and c")
# elif c > a and c > b:
#     print(f"c={c} is greater than a={a} and b={b}")

print("select the options:")
print("1. Add")
print("2. Subtract")
option = int(input("Enter option (1 or 2): "))

if option == 1:
    print("You selected addition.")
    result = a + b
    print(f"The sum of a and b is: {result}")
elif option == 2:
    result = b - a
    print(f"The difference of b and a is: {result}")    
else:
    print("Invalid option selected.")

print("select the options:")
print("1. Database")
print("2. csv file")
print("3. api")
option = int(input("Enter option (1 or 2 or 3): "))

if option == 1:
    print("You selected Database.")
    connection = dbapi.connect(address="your_hana_host",port=30015,  # Or your specific portuser="your_username",password="your_password"
)
    cursor = connection.cursor() # session to connect to the db
    sql_query = "SELECT * FROM table_name"
    cursor.execute(sql_query)
    print(f"SQL Query: {sql_query}")
    cursor.close()
    
elif option == 2:
    print("You selected csv file.")
    file_path = "/path/to/file.csv"
    print(f"File Path: {file_path}")
elif option == 3:
    print("You selected api.")
    api_endpoint = "https://api.example.com/data"
    print(f"API Endpoint: {api_endpoint}")
else:
    print("Invalid option selected.")