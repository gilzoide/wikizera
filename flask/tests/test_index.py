# -*- coding: utf-8 -*-

from tests.test_client_app import ClientAppTestCase

class IndexTest(ClientAppTestCase):
    def test_ping(self):
        res = self.app.get('/ping')
        self.assertStatus(res, 200)
        self.assertJSON(res, 'pong')

    def test_index_route(self):
        res = self.app.get('/')
        self.assertStatus(res, 200)
        self.assertNotJSON(res)
        self.assertIn('**wikizera**', res.get_data())
