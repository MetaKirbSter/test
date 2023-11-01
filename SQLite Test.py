import sqlite3

# Connect to the SQLite database or create a new one if it doesn't exist.
con = sqlite3.connect("college.db")

cur = con.cursor()

# Create a table for the college class system with columns for GPA, class, and credits.
cur.execute("CREATE TABLE IF NOT EXISTS college_class1(grade TEXT, class TEXT, credits INTEGER)")

while True:
    try:
        # Take user inputs for grade, class, and credits.
        grade = input("Enter Grade (Letter): ")
        class_name = input("Enter Class Name: ")
        credits = int(input("Enter Credits: "))
        
        # Insert the user's input into the table.
        cur.execute("INSERT INTO college_class1 VALUES(?, ?, ?)", (grade, class_name, credits))
        con.commit()  # Commit the transaction to save the data in the database.
        
        print("Data inserted successfully.")
        
        # Ask the user if they want to enter more data.
        another_entry = input("Do you want to enter data for another class? (yes/no)? ").strip().lower()
        if another_entry != 'yes':
            break
    except ValueError:
        print("Invalid input. Please enter valid GPA and credits.")

# Query data from the "college_class" table.
cur.execute("SELECT * FROM college_class1")
data = cur.fetchall()

for row in data:
    print("Grade:", row[0])
    print("Class:", row[1])
    print("Credits:", row[2])
    print()

# Close the database connection.
con.close()
