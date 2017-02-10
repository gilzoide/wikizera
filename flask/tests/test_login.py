# -*- coding: utf-8 -*-

from tests.test_client_app import ClientAppTestCase

class LoginTest(ClientAppTestCase):
    def test_login_failure(self):
        res = self.app.json('/login', {
            'email': 'not valid 4 flask-security',
            'password': 'miSenhaEsSuSenha',
        })
        self.assertStatus(res, 400)
