# -*- coding: utf-8 -*-

from flask import Blueprint, request

index_blueprint = Blueprint('index_blueprint', __name__)


@index_blueprint.route('/')
def index():
    return "Quer acessar a **wikizera**? vai pelo front-end, pliz =P"
