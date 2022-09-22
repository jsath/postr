# import the function that will return an instance of a connection
from operator import is_

from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import app
from flask import flash 
from flask_app.models import user

class Like:
    def __init__( self , data ):
        self.posts_id = data['posts_id']
        self.users_id = data['users_id']

    @classmethod
    def save(cls,data):
        query = "INSERT INTO pwall.likes ( posts_id, users_id ) VALUES ( %(posts_id)s, %(users_id)s );"
        status = connectToMySQL('pwall').query_db( query, data )
        return status
    
    @classmethod
    def count(cls, data):
        query = "SELECT COUNT(users_id) FROM pwall.likes where posts_id = %(id)s"
        status = connectToMySQL('pwall').query_db( query, data )
        count = status[0]["COUNT(users_id)"]
        return count


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM pwall.likes WHERE posts_id = %(posts_id)s and users_id = %(users_id)s "
        status = connectToMySQL('pwall').query_db( query, data )
        return status

    @classmethod
    def liked(cls, data):
        query = "SELECT * FROM pwall.likes WHERE posts_id = %(id)s and users_id = %(users_id)s"
        status = connectToMySQL('pwall').query_db( query, data )
        if status:
            print("status is true")
            return True 
        else: 
            print("status is false")
            return False


