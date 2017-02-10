# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_security import Security, MongoEngineUserDatastore
from flask_bootstrap import Bootstrap

from blueprints.index import index_blueprint
import resources.pages
import resources.user
from db import db
from modelos import Role, User
import admin

from os import path


def create_api(app):
    api = Api(app)
    resources.user.setup(api)
    resources.pages.setup(api)
    return api


def create_app(modo='dev'):
    instance_path = path.join(path.abspath('.'), 'instancias', modo)
    # App e blueprints
    app = Flask('wikizera', instance_path=instance_path, instance_relative_config=True)
    app.register_blueprint(index_blueprint)
    # Configurações
    app.config.from_pyfile('config.py')
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
