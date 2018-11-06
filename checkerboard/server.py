from flask import Flask, render_template
app = Flask (__name__)


@app.route("/")
def index ():
    return render_template("index.html", rows=9, columns=9, col1="red", col2="black")


@app.route("/<a>/<b>/")
def WHboard (a,b):
    return render_template("index.html", rows=int(a), columns=int(b), col1="red", col2="black")
    

@app.route("/<a>/<b>/<col1>/<col2>/")
def WHboardCustom (a,b,col1,col2):
    return render_template("index.html", rows=int(a), columns=int(b), col1=col1, col2=col2)

if __name__=="__main__":
    app.run(debug=True)