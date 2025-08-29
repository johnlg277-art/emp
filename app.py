from flask import Flask, request, render_template
from flask_mysqldb import MySQL
import mysql.connector
import webbrowser



app = Flask(__name__)

# MySQL connection setup
db = mysql.connector.connect(
    host="localhost",
    user="root",         # change if different
    password="@admin123", 
    database="company_db"
)
cursor = db.cursor()

# Route for form
@app.route('/')
def index():
    return render_template('index.html')

# Route to insert data
@app.route('/add_employee', methods=['POST'])
def add_employee():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    gender = request.form['gender']
    birth_date = request.form['birth_date']
    hire_date = request.form['hire_date']
    job_title = request.form['job_title']
    department = request.form['department']
    salary = request.form['salary']
    email = request.form['email']
    phone = request.form['phone']

    sql = """
        INSERT INTO employee 
        (first_name, last_name, gender, birth_date, hire_date, job_title, department, salary, email, phone) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (first_name, last_name, gender, birth_date, hire_date, job_title, department, salary, email, phone)

    cursor.execute(sql, values)
    db.commit()

    return "Employee added successfully!"

# NEW: view employees
@app.route('/employees')
def employees():
    cursor.execute("SELECT * FROM company_db.employee")
    rows = cursor.fetchall()
    return render_template('view.html', employee=rows)

if __name__ == '__main__':
    webbrowser.open_new('http://127.0.0.1:5000/')
    app.run(debug=True, port=5000)
