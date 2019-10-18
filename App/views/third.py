from flask import Blueprint

third = Blueprint('The Third', __name__)

@third.route('/third')
def hi():
    return '!Hola Amigo!'