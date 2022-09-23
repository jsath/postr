# import the function that will return an instance of a connection
from operator import is_
from re import L
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import app
from flask import flash 
from flask_app.models import user
from flask_app.models.comment_like import Comment_Like

class Comment:
    def __init__( self , data ):
        self.comment_id = data['comment_id']
        self.post_id = data['post_id']
        self.user_id = data['user_id']
        self.parent_id = data['parent_id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod 
    def get_post_comments(cls, data):
        query = "SELECT comments.comment, comments.comment_id, users.first_name FROM pwall.comments Left Join users on comments.user_id = users.id where post_id = %(id)s;"
        results = connectToMySQL('pwall').query_db( query, data )
    

        comments = []
        for comment in results:
            data2 = { 
            'post_id': data['id'],
            'comment_id': comment['comment_id'],
            'user_id' : data['users_id']
            }
            
            comment['count'] = Comment_Like.count(data2)
            comment['liked'] = Comment_Like.liked(data2)
            comments.append(comment)
        
        
        return comments

    @classmethod 
    def display_comment(cls, data):
        query = "SELECT comments.comment, comments.comment_id, users.first_name FROM pwall.comments Left Join users on comments.user_id = users.id where post_id = %(id)s LIMIT 1;"
        results = connectToMySQL('pwall').query_db( query, data )


        comments = []
        for comment in results:
            data2 = { 
            'post_id': data['id'],
            'comment_id': comment['comment_id'],
            'user_id' : data['users_id']
            }
            comment['count'] = Comment_Like.count(data2)
            comment['liked'] = Comment_Like.liked(data2)
            comments.append(comment)
        
        return comments
    
    @classmethod
    def create_comment(cls, data):
        query = "INSERT into pwall.comments(post_id, user_id, comment, created_at, updated_at) values(%(post_id)s, %(user_id)s, %(comment)s, NOW(), NOW());"
        results = connectToMySQL('pwall').query_db( query, data )
        return results 
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["comment"]) < 2:
            is_valid = False
            flash("Comment too short!")
        return is_valid
    