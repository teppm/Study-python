import os
import json
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/about")

def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")

def contact():
    return render_template("contact.html", page_title="Contacts")


@app.route("/careers")

def careers():
    return render_template("careers.html", page_title="Join our team!")