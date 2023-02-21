from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB
from flask import flash
from flask_app.models import vehicle_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.cin = data['cin']
        self.password = data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod #register an account
    def register(cls, data):
        query = """
                INSERT INTO users (first_name, last_name, email, cin, password) 
                VALUES (%(first_name)s, %(last_name)s, %(email)s, %(cin)s, %(password)s)
                """
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod #! search user by email
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result= connectToMySQL(DB).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    
    @classmethod #! Update profile
    def get_by_email(cls, data):
        query = """UPDATE tv_shows SET title=%(title)s,
                network=%(network)s,release_date=%(release_date)s,description=%(description)s
                WHERE id=%(id)s;"""
        result= connectToMySQL(DB).query_db(query,data)
        if len(result)<1:
            return False
        return cls(result[0])
    



    @staticmethod
    def validate_user(data):
        is_valid = True
        if len(data['first_name'])<2:
            is_valid = False
            flash("Invalid first name, must be greater than 2 characters!", "first_name")
        if len(data['last_name'])<2:
            is_valid = False
            flash("Invalid last name, must be greater than 2 characters!", "last_name")
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "email")
            is_valid = False
        elif User.get_by_email({'email': data['email']}):
            is_valid = False
            flash("email address already exists!", "email")
        if  len(data['cin'])!=8:
            flash("Invalid cin code!", "cin")
            is_valid = False
        if len(data['password'])<8:
            is_valid = False
            flash("Invalid password, must be greater than 8 characters!", "password")
        elif data['password']!=data['confirm_password']:
            flash("Password and confirm_password must match!", "confirm_password")
            is_valid = False
        return is_valid