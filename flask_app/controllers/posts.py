from crypt import methods
from flask_app import app
from flask import render_template,redirect,request, session
from flask_app.models.user import User
from flask_app.models.message import Message 
from flask_app.models.post import Post
from flask_app.models.like import Like
from flask_app.models.comment import Comment
from flask_app.models.comment_like import Comment_Like



@app.route('/home')
def home():
    if session["access"] == False:
        return redirect('/')

    data = {
        'users_id' : session['id']
    }
    first = session["name"] 
    posts = Post.get_all(data)
    return render_template("home.html",first=first, posts=posts)

@app.route('/addpost')
def add():

    return render_template("addpost.html")

@app.route('/post', methods=['POST'])
def create():

    data = {
        'title': request.form['title'],
        'content' : request.form['content'],
        'user_id' : session['id']
    }
    if not Post.validate(data):
        return redirect("/addpost")
    Post.save(data)
    return redirect('/home')

@app.route('/like/<int:posts_id>/<int:users_id>')
def like(posts_id, users_id):
    data = {
        "posts_id" : posts_id, 
        "users_id" : users_id
    }
    Like.save(data)
    return redirect('/home')


@app.route('/unlike/<int:posts_id>/<int:users_id>')
def unlike(posts_id, users_id):
    data = {
        "posts_id" : posts_id, 
        "users_id" : users_id
    }
    Like.delete(data)
    return redirect('/home')

@app.route('/like2/<int:posts_id>/<int:users_id>')
def like2(posts_id, users_id):
    data = {
        "posts_id" : posts_id, 
        "users_id" : users_id
    }
    Like.save(data)
    return redirect(f'/display/{posts_id}')

@app.route('/unlike2/<int:posts_id>/<int:users_id>')
def unlike2(posts_id, users_id):
    data = {
        "posts_id" : posts_id, 
        "users_id" : users_id
    }
    Like.delete(data)
    return redirect(f'/display/{posts_id}')

@app.route('/display/<int:id>')
def displaypost(id):
    data = {
        "id" : id,
        "users_id" : session['id']
    }
    post = Post.get_one(data)
    return render_template("displaypost.html", post=post)




@app.route('/addcomment/<int:post_id>', methods=['POST'])
def add_comment(post_id):

    data = { 
        'post_id': post_id, 
        'user_id': session['id'],
        'comment' : request.form['comment']
    }

    Comment.create_comment(data)

    return redirect('/home')

@app.route('/addcomment2/<int:post_id>', methods=['POST'])
def add_comment2(post_id):

    data = { 
        'post_id': post_id, 
        'user_id': session['id'],
        'comment' : request.form['comment']
    }

    Comment.create_comment(data)

    return redirect(f'/display/{post_id}')


@app.route('/commentlike/<int:posts_id>/<int:users_id>/<int:comment_id>')
def comment_like(posts_id, users_id, comment_id):
    data = {
        "post_id" : posts_id, 
        "users_id" : users_id, 
        "comment_id": comment_id
    }
    Comment_Like.save(data)
    return redirect('/home')


@app.route('/commentunlike/<int:posts_id>/<int:users_id>/<int:comment_id>')
def comment_unlike(posts_id, users_id, comment_id):
    data = {
        "comments_post_id" : posts_id, 
        "users_id" : users_id, 
        "comments_comment_id": comment_id
    }
    Comment_Like.delete(data)
    return redirect('/home')


@app.route('/commentlike2/<int:posts_id>/<int:users_id>/<int:comment_id>')
def comment_like2(posts_id, users_id, comment_id):
    data = {
        "post_id" : posts_id, 
        "users_id" : users_id, 
        "comment_id": comment_id
    }
    Comment_Like.save(data)
    return redirect(f'/display/{posts_id}')


@app.route('/commentunlike2/<int:posts_id>/<int:users_id>/<int:comment_id>')
def comment_unlike2(posts_id, users_id, comment_id):
    data = {
        "comments_post_id" : posts_id, 
        "users_id" : users_id, 
        "comments_comment_id": comment_id
    }
    Comment_Like.delete(data)
    return redirect(f'/display/{posts_id}')


@app.route('/favorites')
def favorites():

    data = {
        "id" : session['id']
    }

    posts = Post.get_liked(data)
    return render_template("favorites.html", posts=posts)

