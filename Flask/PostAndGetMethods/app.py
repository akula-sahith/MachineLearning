from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/index')
def welcome():
    return render_template('index.html')

@app.route('/filltheform',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

@app.route('/submit',methods=['GET'])
def submit():
    if(request.method=="post"):
        name = request.form['name']
        return f"Hello {name}"
    return render_template('form.html')
   
if __name__=="__main__":
    app.run(debug=True)