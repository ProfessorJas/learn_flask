from flask import Flask
from App.views import init_view

# from App.views import init_route
# from App.views import blue, second

def create_app():
    app = Flask(__name__)

    # init_route(app)
    # app.register_blueprint(blue)

    # app.register_blueprint(second)

    init_view(app)
    return app