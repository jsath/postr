# import the function that will return an instance of a connection
from operator import is_
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import app
from flask import flash 
from flask_bcrypt import Bcrypt
import re
bcrypt = Bcrypt(app)  


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO pwall.users ( first_name, last_name, email, password, created_at, updated_at ) VALUES ( %(first_name)s , %(last_name)s , %(email)s , %(password)s, NOW() , NOW() )"
        status = connectToMySQL('pwall').query_db( query, data )
        return status


    @staticmethod 
    def login(data): 
        email = True
        query = "SELECT users.password from pwall.users WHERE email = %(email)s"
        status = connectToMySQL('pwall').query_db( query, data )
        if not status: 
            flash("Login Error: Please register First")
            email = False
        return email


    @staticmethod
    def confirm(data):
        is_valid = True 
        if (data['password'] != data['confirm_password']):
            flash("Passwords don't match!")
            is_valid = False
        elif len(data["password"]) < 8:
            flash("Password must be at least 8 characters!")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("First name must contain more than 2 characters!")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must contain more than 2 characters!")
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email format!")
            is_valid = False
        elif len(data['email']) < 5:
            flash("Email must contain more than 5 characters!")
            is_valid = False
        return is_valid
    
    @staticmethod 
    def check(data):
        check = True
        query = "SELECT users.password from pwall.users WHERE email = %(email)s"
        status = connectToMySQL('pwall').query_db( query, data )
        email_password = status[0]['password']
        if not bcrypt.check_password_hash(email_password, data["password"]):
            flash("Login Error: Your password doesn't match")
            check = False 
        return check
    
    @classmethod 
    def name(cls, data):
        query = "SELECT users.first_name from users WHERE email = %(email)s"
        status = connectToMySQL('pwall').query_db( query, data )
        name = status[0]['first_name']
        return name
    
    @staticmethod
    def register(data):
        valid = True
        query = "SELECT users.email from users WHERE email = %(email)s"
        status = connectToMySQL('pwall').query_db( query, data )
        if status: 
            flash("Email already exists!Login")
            valid = False 
    
        return valid 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('pwall').query_db(query)

        users = []
        for user in results: 
            users.append(cls(user)) 
        return users



    @classmethod 
    def id(cls, data):
        query = "SELECT users.id from users WHERE email = %(email)s"
        status = connectToMySQL('pwall').query_db( query, data )
        id = status[0]['id']
        return id
    
    @classmethod
    def get_name(cls, data):
        query = "SELECT first_name from users WHERE id = %(user_id)s"
        results = connectToMySQL('pwall').query_db( query, data )
        return results[0]['first_name']
    
