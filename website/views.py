from flask import Blueprint

views = Blueprint("views", __name__)

@views.route('/')
def mainroute():
    return "<h1>Hello world"

@views.route('/login')
def login():
    return "<h1>Login to the website"