# -*- coding: utf-8 -*-

from tests.ClientApp import test_app
from wikizera.modelos import User, Pagina

import unittest


CLIENTE_TESTE = {
    'email': 'teste@teste.com',
    'password': '123123',
}

class ClientTestCase(unittest.TestCase):
    """TestCase que já tem app sabe dar assert de status_code HTTP"""

    def setUp(self):
        self.app = test_app
        self.app.json('/register', data=CLIENTE_TESTE)

    def tearDown(self):
        User.drop_collection()
        Pagina.drop_collection()

    def assertStatus(self, response, expected_code):
        """Assert customizado, pra código de status de resposta HTTP"""
        self.assertEqual(response.status_code, expected_code)

    def _post_login(self):
        """Faz a requisição POST pro /login com dados que é pra rolar"""
        return self.app.json('/login', data=CLIENTE_TESTE)

    def do_login(self):
        """Faz o login de fato, pra facilitar o teste de rotas com token"""
        res = self._post_login()
        self.assertStatus(res, 302)

    def test_do_login(self):
        self.do_login()
