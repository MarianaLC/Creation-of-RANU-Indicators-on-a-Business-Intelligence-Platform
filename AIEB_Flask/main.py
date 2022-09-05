from flask import Flask, render_template, request
import re
import json
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("login.html")
    
@app.route("/powerbi")
def home():
    return render_template("teste_AIEB.html")

@app.route("/tableau")
def tableau():
    return render_template("tableau.html")


app.run(port=4000, debug=True) 
