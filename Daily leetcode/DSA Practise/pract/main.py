from flask import Flask,render_template,request,url_for
app=Flask(__name__)
@app.route("/")
def base():
    return render_template("index.html")
@app.route("/result",methods=["GET","POST"])
def res():
    if request.method=="POST":
        res=request.form
        return render_template("result.html",result=res)
app.run(debug=True)