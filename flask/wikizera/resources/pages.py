# -*- coding: utf-8 -*-

from flask import request
from flask_restful import Resource, reqparse
from flask_security import auth_token_required, current_user

from wikizera.modelos import Pagina


save_page_parser = reqparse.RequestParser()
save_page_parser.add_argument('name', required=True)
save_page_parser.add_argument('content', required=True)
save_page_parser.add_argument('id')


class PageListResource(Resource):
    @auth_token_required
    def get(self):
        return current_user.pages

    @auth_token_required
    def post(self):
        args = save_page_parser.parse_args()
        if args.id:
            Pagina.objects().filter(id=args.id).upsert_one(name=args.name,
                                                           content=args.content)
            return {'success': 'Página salva!'}


class PageResource(Resource):
    @auth_token_required
    def get(self, page_id):
        try:
            return next(p for p in current_user.pages if p.id == page_id)
        except StopIteration:
            return {'error': 'Página não existe pro usuário'}




def setup(api):
    api.add_resource(PageListResource, '/my-pages')
    api.add_resource(PageResource, '/my-pages/<int:page_id>')
