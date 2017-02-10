# -*- coding: utf-8 -*-

from wikizera.app import create_app
from wikizera.modelos import User, Pagina
from tests.test_case import ClientTestCase

import json

# The test application to use across all tests, it's always the same =]
test_app = create_app('test').test_client()

def _post_json(self, url, data, *args, **kwargs):
    kwargs['content_type'] = 'application/json'
    return self.post(url, data=json.dumps(data), *args, **kwargs)

# Função extra pra mandar JSON por POST
test_app.__class__.json = _post_json

# Cliente de teste, um que sempre existe
CLIENTE_TESTE = {
    'email': 'teste@teste.com',
    'password': '123123',
}

class ClientAppTestCase(ClientTestCase):
    """TestCase que cria um usuário no setup e limpa o bd no teardown"""

    def setUp(self):
        self.app = test_app
        self.app.json('/register', CLIENTE_TESTE)

    def tearDown(self):
        User.drop_collection()
        Pagina.drop_collection()

    def _post_login(self):
        """Faz a requisição POST pro /login com dados que é pra rolar"""
        return self.app.json('/login', CLIENTE_TESTE)

    def do_login(self):
        """Faz o login de fato, pra facilitar o teste de rotas com token"""
        return self._post_login()

    def test_do_login(self):
        res = self.do_login()
        self.assertStatus(res, 302)
