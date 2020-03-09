from flask import Flask
from flask_simpleldap import LDAP

from main.util.config import LDAPConfig

ldap = LDAP()


def create_app():
    """Creates the flask app
    """
    app = Flask(__name__)
    configure_app(app, LDAPConfig)
    register_extensions(app)
    return app


def configure_app(app, config=None):
    """configures the flask app from a config file

    :param app: Flask App
    :type app: Flask
    :param config: A config Class, defaults to None
    :type config: Class, optional
    :raises FileNotFoundError: Config class not found
    """
    if config:
        app.config.from_object(config)
    else:
        raise FileNotFoundError()


def register_extensions(app):
    """Initialises the Flask app with LDAP Auth

    :param app: Flask app
    :type app: Flask
    """
    ldap.init_app(app)
