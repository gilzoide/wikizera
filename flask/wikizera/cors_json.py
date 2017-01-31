# -*- coding: utf-8 -*-

from flask import jsonify


def cors_json(*args, **kwargs):
    """Cria uma resposta JSONificada com o header que possibilita requisição CORS"""
    res = jsonify(*args, **kwargs)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res
