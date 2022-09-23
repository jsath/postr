# import the function that will return an instance of a connection
from operator import is_
from re import L
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import app
from flask import flash 
from flask_app.models import user

class Comment_Like:
    def __init__( self , data ):
        self.comments_comment_id = data['comments_comment_id']
        self.comments_post_id = data['comments_post_id']
        self.users_id = data['users_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    

    @classmethod
    def save(cls,data):
        query = "INSERT INTO pwall.comments_likes ( comments_comment_id, comments_post_id, users_id, created_at, updated_at ) VALUES ( %(comment_id)s, %(post_id)s, %(users_id)s, NOW(), NOW() );"
        status = connectToMySQL('pwall').query_db( query, data )
        print(status)
        return status
    
    @classmethod
    def count(cls, data):
        query = "SELECT COUNT(users_id) FROM pwall.comments_likes WHERE comments_post_id = %(post_id)s and comments_comment_id = %(comment_id)s;"
        status = connectToMySQL('pwall').query_db( query, data )
        count = status[0]["COUNT(users_id)"]
        print(count)
        return count


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pwall.comments_likes WHERE comments_post_id = %(comments_post_id)s and users_id = %(users_id)s and comments_comment_id = %(comments_comment_id)s; "
        status = connectToMySQL('pwall').query_db( query, data )
        return status

    @classmethod
    def liked(cls, data):
        query = "SELECT * FROM pwall.comments_likes WHERE comments_post_id = %(post_id)s and users_id = %(user_id)s and comments_comment_id = %(comment_id)s"
        status = connectToMySQL('pwall').query_db( query, data )
        if status:
            return True 
        else: 
            return False
