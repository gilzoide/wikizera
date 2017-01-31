# -*- coding: utf-8 -*-

from flask import Flask
from flask_security import Security, MongoEngineUserDatastore
from flask_bootstrap import Bootstrap

from blueprints.index import index_blueprint
from blueprints.user import user_blueprint
from db import db
from modelos import Role, User
import admin

from os import path


def create_app(modo='dev'):
    instance_path = path.join(path.abspath('.'), 'instancias', modo)
    # App e blueprints
    app = Flask('wikizera', instance_path=instance_path, instance_relative_config=True)
    app.register_blueprint(index_blueprint)
    app.register_blueprint(user_blueprint)
    # Configurações
    app.config.from_pyfile('config.py')
    # Plugins
    db.init_app(app)
    Bootstrap(app)
    Security(app=app, datastore=MongoEngineUserDatastore(db, User, Role))
    admin.configura(app)
    return app
