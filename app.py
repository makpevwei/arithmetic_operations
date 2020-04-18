from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
@app.route('/input')
def index():
    return render_template("arithmetic_input.html")


@app.route('/addition',methods=["GET", "POST"])
def addition():
    
    if request.method == "POST":
        fn = request.form.get("fn")
        sn = request.form.get("sn")

        return render_template('addition_result.html' , response = str(float(fn) + float(sn)))
    

if __name__ == '__main__':
    app.run()