
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

    Message.new_message(data)
    return redirect(f"/messages/{session['messageid']}")


@app.route("/messages/<int:id>")
def messages(id):
    if session["access"] == False:
        return redirect('/')
    first = session["name"] 
    messages = Message.get_all()
    users = User.get_all()

    data = { 
        "id" : session['id'],
        "user_id" : id
    }

    session['messageid'] = data['user_id']
    if id != 0:
        texts = Message.display(data)
        id = session['messageid']
        name = User.get_name(data)
        return render_template('messages2.html', texts=texts, users=users, id=id, name=name)

    unread = Message.unread(data)
    return render_template("messages2.html", users=users, unread=unread)

