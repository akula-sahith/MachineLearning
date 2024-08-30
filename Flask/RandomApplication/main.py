from flask import Flask, render_template, request ,g
import sqlite3

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.connection = sqlite3.connect('Database.db')
    return g.connection

@app.route('/read', methods=['GET','POST'])
def read():
    if request.method == "POST":
        name_from_form = request.form['name']
        roll_from_form = request.form['roll']
        dept_from_form = request.form['dept']
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS DATA(
                        Name text NOT NULL,
                        RollNumber int PRIMARY KEY,
                        Department text NOT NULL)''')
        connection.commit()
        cursor.execute('INSERT INTO DATA (name,RollNumber,Department) VALUES (?,?,?)', (name_from_form,roll_from_form,dept_from_form))
        connection.commit()
        return f"{name_from_form} was stored into database"
    else:
        return render_template('login.html')

@app.route('/get',methods=['GET','POST'])
def give():
    if request.method == "POST":
        roll_from_form = request.form['roll']
        connection = get_db()
        cursor = connection.cursor()
        cursor.execute('''SELECT * from DATA
                          WHERE RollNumber = ?
                       ''',(roll_from_form,))
        rows = cursor.fetchall()
        name = rows[0][0]
        rollnumber = rows[0][1]
        department = rows[0][2]
        data = {"name":name,"Roll Number":rollnumber,"Department":department}
        return render_template('displaydetails.html',details = data)
    return render_template('getdetails.html')

if __name__ == "__main__":
    app.run(debug=True)
