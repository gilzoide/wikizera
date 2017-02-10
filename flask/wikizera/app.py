# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_security import Security, MongoEngineUserDatastore
from flask_bootstrap import Bootstrap

from wikizera.blueprints.index import index_blueprint
import wikizera.resources.pages as pages
import wikizera.resources.user as user
import wikizera.resources.ping as ping
from wikizera.db import db
from wikizera.modelos import Role, User
import wikizera.admin as admin
from wikizera.utf_response import Utf8Response

from os import path


def create_api(app):
    api = Api(app)
    user.setup(api)
    pages.setup(api)
    ping.setup(api)
    return api


def create_app(modo='dev'):
    instance_path = path.join(path.abspath('.'), 'instancias', modo)
    # App e blueprints
    app = Flask('wikizera', instance_path=instance_path, instance_relative_config=True)
    app.register_blueprint(index_blueprint)
    # Configurações
    app.config.from_pyfile('config.py')
    # UTF-8 por padrão xD
    app.response_class = Utf8Response
    # Plugins
    CORS(app, origins=[app.config['WIKIZERA_REACT_ORIGIN']])
    db.init_app(app)
    Bootstrap(app)
    admin.configura(app)
    create_api(app)
    # Segurança
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    Security(app=app, datastore=user_datastore)
    return app
