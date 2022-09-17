from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.message import Message 

@app.route("/news")
def news():
    return render_template("news.html")