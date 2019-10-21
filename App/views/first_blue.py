from flask import Blueprint, render_template

from App.models import models

blue = Blueprint('blue', __name__)

@blue.route('/')
def index():
    # return 'I am Blue Printer'
    return render_template('index.html', msg = "AMIGO is my friend")

@blue.route('/createdb/')
def createdb():
    models.create_all()

    return "Create DB Successfully"