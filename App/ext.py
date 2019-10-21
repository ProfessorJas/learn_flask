from flask_sqlalchemy import SQLAlchemy

models = SQLAlchemy()

def int_ext(app):
    models.init_app(app)