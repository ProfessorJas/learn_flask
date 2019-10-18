from .first_blue import blue
from .second_blue import second
from .third import third

# def init_route(app):
#     @app.route('/')
#     def hello_world():
#         return "Hello World!"

#     @app.route('/hello')
#     def hello():
#         return "Hola Amigo"

#     @app.route('/hi')
#     def hi():
#         return "JAJAJA"

def init_view(app):
    app.register_blueprint(blue)
    app.register_blueprint(second)
    app.register_blueprint(third)