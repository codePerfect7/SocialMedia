from flask import Flask

def createapp():
    #Initializing the app
    app = Flask(__name__)

    #Making the routes
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    #Returning the app
    return app