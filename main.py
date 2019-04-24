import os
from flask import Flask,jsonify,flash, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import algorithms
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'doc', 'docx', 'pdf'])

app = Flask(__name__)
app.secret_key = "super secret key"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_result(algo, text1, text2):
    if algo == "LCStr":
        return algorithms.LCStr(text1, text2)
    elif algo == "LCSeq":
        return algorithms.LCSeq(text1, text2)
    elif algo == "Jaro":
        return algorithms.Jaro(text1, text2)
    elif algo == "Jaro–Winkler":
        return algorithms.Jaro_Winkler(text1, text2)
    elif algo == "Levenshtein":
        return algorithms.Levenshtein(text1, text2)
    elif algo == "Damerau-Levenshtein":
        return algorithms.Damerau_Levenshtein(text1, text2)
    elif algo == "Ratcliff/Obershelp":
        return algorithms.Ratcliff_Obershelp(text1, text2)
    elif algo == "Fuzzy":
        return algorithms.Fuzzy(text1, text2)
    elif algo=="nn":
        return algorithms.NeuralNetwork(text1, text2)




@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/calculate",methods=["GET", "POST"])
def calculate():
    text1 = request.form["text_a"]
    text2 = request.form["text_b"]
    algo = request.form['algo']
    result=get_result(algo,text1,text2)
    print(text1, text2, algo,result)
    if(result!="s" and result!="ns"):
        result=round(result)
    return jsonify(result=result, algo=algo)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
