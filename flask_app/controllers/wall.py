
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.message import Message 
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    session["access"] = False 
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data = { 
        "first_name" : request.form["first_name"], 
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "confirm_password" : request.form["confirm_password"]
    }
    if not User.confirm(data):
        return redirect('/')
    if not User.register(data):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form["password"])
    data2 = { 
        "first_name" : request.form["first_name"], 
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }
    User.save(data2)
    session["name"] = request.form["first_name"]
    session["id"] = User.id(data)
    session["access"] = True
    return redirect("/home")

@app.route('/home')
def home():
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

    return render_template("home.html", first=first, messages=messages, users=users, unread=unread, sent=sent)

@app.route('/login', methods=['POST'])
def login():
    data = { 
        "email": request.form["email"],
        "password" : request.form["password"]
    }

    if not User.login(data):
        return redirect("/")
    if not User.check(data):
        return redirect("/")
    session["name"] = User.name(data)
    session["id"] = User.id(data)
    session["access"] = True
    return redirect("/home")

@app.route('/logout')
def logout(): 
    del session["name"]
    del session['id']
    session["access"] = False
    return redirect("/")

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


