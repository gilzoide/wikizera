# -*- coding: utf-8 -*-

import unittest
import json


class ClientTestCase(unittest.TestCase):
    """TestCase que já tem app sabe dar assert de status_code HTTP"""

    def assertStatus(self, response, expected_code):
        """Assert customizado, pra código de status de resposta HTTP"""
        self.assertEqual(response.status_code, expected_code)

    def assertJSON(self, response, expected_object):
        """Assert customizado pra resposta JSON"""
        self.assertEqual(response.content_type, 'application/json', "Resposta HTTP não tem conteúdo JSON")
        self.assertEqual(json.loads(response.get_data()), expected_object)

    def assertNotJSON(self, response):
        self.assertNotEqual(response.headers['Content-Type'], 'application/json')
