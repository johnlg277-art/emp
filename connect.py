import mysql.connector

# connect to database
db = mysql.connector.connect(
    host="localhost",
    user="root",          # change if different
    password="@admin123",  # change to your MySQL password
    database="company_db"
)

cursor = db.cursor(dictionary=True)  # get results as dictionary

# fetch employees
cursor.execute("SELECT * FROM company_db.employee")
rows = cursor.fetchall()

print("Employees in database:")
for row in rows:
    print(row)

db.close()
