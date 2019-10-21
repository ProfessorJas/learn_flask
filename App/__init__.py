from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from App.ext import init_ext
from App.views import init_view

# from App.views import init_route
# from App.views import blue, second

def create_app():
    app = Flask(__name__)

    # init_route(app)
    # app.register_blueprint(blue)

    # app.register_blueprint(second)

    # uri   database+driver://username:password@machine:port/
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqite.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_ext()

    init_view(app)
    
    return app