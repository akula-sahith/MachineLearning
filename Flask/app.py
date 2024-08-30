from flask import Flask

app = Flask(__name__) #Web server gateway interface

@app.route('/home')
def welcome():
    return "Welcome to flask"

@app.route('/index')
def index():
    return "Welcome to index page"

if __name__=="__main__":
    app.run(debug=True)