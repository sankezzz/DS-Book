from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to flask app "

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'hello {name} welcome here'
    
    return render_template("form.html")

@app.route('/success/<int:score>')
def success(score):
    res=''
    if score>50:
        res="passed"
    else:
        res="failed"
    return render_template ('result.html',result=res)

if __name__=="__main__":
    app.run(debug=True)