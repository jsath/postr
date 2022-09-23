from operator import is_
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import app
from flask import flash 
from flask_app.models.like import Like
from flask_app.models.comment import Comment
from flask_app.models.comment_like import Comment_Like


class Post:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO pwall.posts ( title, content, created_at, updated_at, user_id ) VALUES ( %(title)s , %(content)s , NOW() , NOW(), %(user_id)s );"
        status = connectToMySQL('pwall').query_db( query, data )
        return status
    
    @classmethod 
    def get_all(cls, data):
        query = "SELECT title, content, posts.created_at, first_name, posts.id FROM pwall.posts JOIN users on users.id= posts.user_id ORDER BY posts.created_at DESC;"
        results = connectToMySQL('pwall').query_db(query)

        posts = []
        for post in results: 
            data2 = { 
                'id' : post['id'],
                'users_id' : data['users_id']
            }
            post['likes'] = Like.count(data2)
            post['liked'] = Like.liked(data2)
            post['comments'] = Comment.display_comment(data2)
            posts.append(post)
        return posts
    

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["content"]) < 20:
            is_valid = False
            flash("Post Content must be longer than 20 characters")
        return is_valid
    
    @classmethod
    def get_one(cls, data):
        query = 'SELECT title, content, posts.created_at, first_name, posts.id FROM pwall.posts JOIN users on users.id= posts.user_id  where posts.id = %(id)s'
        status = connectToMySQL('pwall').query_db( query, data )
        post = status[0]
        data2 = { 
                'id' : post['id'],
                'users_id' : data['users_id']
            }
        post['likes'] = Like.count(data2)
        post['liked'] = Like.liked(data2)
        post['comments'] = Comment.get_post_comments(data2)

        return post

    @classmethod 
    def get_liked(cls, data):
        query = "SELECT title, content, posts.created_at, first_name, posts.id, likes.users_id FROM pwall.posts JOIN users on users.id= posts.user_id join likes on likes.posts_id = posts.id WHERE likes.users_id = %(id)s"
        results = connectToMySQL('pwall').query_db( query, data )

        posts = []
        for post in results: 
            data2 = { 
                'id' : post['id'],
                'users_id' : data['id']
            }
            post['likes'] = Like.count(data2)
            post['liked'] = Like.liked(data2)
            post['comments'] = Comment.display_comment(data2)
            posts.append(post)
        return posts
    
