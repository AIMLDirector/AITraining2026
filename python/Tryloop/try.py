try:
    a =int("test")
except ValueError as ve:
    print("Value error occurred:", ve)

import logging
try:
    file = open("non_existent_file.txt", "r")
    print(file.read())
except FileNotFoundError as fnfe:
    print(fnfe)
    logging.error("File not found error: %s", fnfe)

try:
    file = open("non_existent_file.txt", "r")
    print(file.read())
except (FileNotFoundError, ZeroDivisionError) as e:
    print("An error occurred:", e)
except ValueError as ve:
    print("Value error occurred:", ve)
finally:


import sqlite3 # Or your specific database connector (e.g., psycopg2, mysql.connector)

def connect_and_query(db_name="mydatabase.db"):
    conn = None  # Initialize connection to None
    try:
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
        conn.commit()
        print("Data inserted successfully.")
    except sqlite3.OperationalError as e:
        print(f"Database operational error: {e}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        if conn:
            conn.rollback() # Rollback changes on error
    finally:
        if conn:
            conn.close()
            print("Database connection closed.")

connect_and_query()


import logging 

logging.info("input value variables from tryloop.py :",var1)
logging.warning("This is a warning message.")
logging.error("This is an error message.")
logging.debug("This is a debug message.")
logging.CRITICAL("This is a critical message.")

try:
    v1 = int(input("Enter a number: "))
except ValueError as ve:
    logging.error("Invalid input. Please enter a valid integer.")
    print(ve)
else:
    if v1 % 2 == 0:
        print(f"{v1} is an even number.")
    else:
        print(f"{v1} is an odd number.")

# try (successfull) -> else 
# try(failure) -> except  






