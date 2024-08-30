from flask import Flask,render_template,request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/FlaskApplication"

# Step 4: Initialize PyMongo
mongo = PyMongo(app)

@app.route('/read',methods=['GET','POST'])
def read():
    if request.method=="POST":
        user_data = {
         "name": request.form['name'],
         "RollNumber": request.form['roll'],
         "Gender" : request.form['gender']
        }
        mongo.db.Students.insert_one(user_data)
    return render_template('Form.html')

@app.route('/show',methods=['GET','POST'])
def show():
    if request.method=="POST":
        user_data = {
         "RollNumber": request.form['roll']
        }
        user = mongo.db.Students.find_one(user_data)
        return render_template('Showdetails.html',data = user)
    return render_template('Login.html')
  
if __name__=="__main__":
    app.run(debug=True)