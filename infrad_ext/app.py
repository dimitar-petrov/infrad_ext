from flask import Flask

from infrad_ext.rest import command_result
from infrad_ext.settings import DevConfig

def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(command_result.blueprint)
    return app
