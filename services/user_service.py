from flask import request
from controllers import users_controller

def validate_user():
    username = request.form['username']
    password = request.form['password']
    return users_controller.get_user(username, password)