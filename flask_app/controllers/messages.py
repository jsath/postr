
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.message import Message 


@app.route("/send/<int:id>", methods=["POST"])
def send(id):
    
    data = { 
        "content" : request.form["content"], 
        "send_to" : id, 
        "user_id" : session['id']
    }
    if not Message.validate(data):
        return redirect("/home")
    Message.new_message(data)
    return redirect("/home")

@app.route("/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    Message.delete(data)
    return redirect("/home")


@app.route("/messages")
def messages():
    if session["access"] == False:
        return redirect('/')
    first = session["name"] 
    messages = Message.get_all()
    users = User.get_all()

    data = { 
        "id" : session['id']
    }

    unread = Message.unread(data)
    sent = Message.sent(data)
    return render_template("messages.html", first=first, messages=messages, users=users, unread=unread, sent=sent)
