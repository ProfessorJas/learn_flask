from flask import Blueprint

second = Blueprint('second', __name__)

@second.route('/second')
def hello():
    return "Second Blue"