import flask
from router import main_router
from api import api
def create_app():
    app = flask.Flask(
            __name__,
            static_url_path='/public',
            static_folder='./templates/public/',
            template_folder='./templates',
          )

    database = {
            "users": {
                "berstearns@gmail.com": {
                    "username": "berstearns@gmail.com",
                    "password": "ber123",
                    }
            }
    }
    sessions = {
            "ajiosf12j3oi1ih41o" : "berstearns@gmail.com"
    }

    app.database = database
    app.sessions = sessions

    app.register_blueprint(main_router)
    app.register_blueprint(api)
    return app
