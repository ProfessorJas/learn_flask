from flask import Blueprint, render_template

blue = Blueprint('blue', __name__)

@blue.route('/')
def index():
    # return 'I am Blue Printer'
    return render_template('index.html')