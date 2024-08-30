from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/submit/<int:score>')
def submit(score):
    res = ""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"

    return render_template('result.html',results = res)

@app.route('/submit2/<int:score>')
def submit2(score):
    res = ""
    if score>=55:
        res = "PASSED"
    else:
        res = "FAILED"
    data = {"score":score,"result":res}
    return render_template('result2.html',results = data)

if __name__=="__main__":
    app.run(debug=True)
