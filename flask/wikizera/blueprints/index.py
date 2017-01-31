# -*- coding: utf-8 -*-

from flask import Blueprint

from wikizera.cors_json import cors_json

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/')
def index():
    return cors_json("Quer acessar a wikizera? vai pelo front-end, pliz =P")
