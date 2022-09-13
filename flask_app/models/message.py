# import the function that will return an instance of a connection
from operator import is_
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import app
from flask import flash 
from flask_app.models import user

class Message:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.send_to = data['send_to']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM messages JOIN users ON messages.user_id = users.id "
        results = connectToMySQL('pwall').query_db(query)

        messages = []
        for message in results:
            messageactual = cls(message)
            user_data = { 
                "first_name" : message['first_name'],
                "last_name" : message['last_name'],
                "email" : message['email'],
                "password" : message['password'],
                "id" : message['users.id'],
                "updated_at" : message['users.updated_at'],
                "created_at": message['users.created_at']
            }
            useractual = user.User(user_data)
            messageactual.user = useractual 
            messages.append(messageactual) 
        return messages
    
    @classmethod 
    def new_message(cls, data):
        query = "INSERT into pwall.messages(content, send_to, created_at, updated_at, user_id) values(%(content)s, %(send_to)s, NOW(), NOW(), %(user_id)s)"
        status = connectToMySQL('pwall').query_db( query, data )
        return status
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM messages WHERE messages.id = %(id)s"
        status = connectToMySQL('pwall').query_db( query, data )
        return status
    
    @classmethod 
    def unread(cls, data):
        query = "SELECT COUNT(content) FROM messages where messages.send_to = %(id)s"
        status = connectToMySQL('pwall').query_db( query, data )
        count = status[0]["COUNT(content)"]
        return count

    @classmethod 
    def sent(cls, data):
        query = "SELECT COUNT(content) FROM messages where messages.user_id = %(id)s"
        status = connectToMySQL('pwall').query_db( query, data )
        count = status[0]["COUNT(content)"]
        return count
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["content"]) < 5:
            is_valid = False
            flash("Message must be longer than 5 characters!")
        
        return is_valid
