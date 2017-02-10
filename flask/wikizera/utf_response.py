# -*- coding: utf-8 -*-

from flask import Response

import json


class Utf8Response(Response):
    """Subclasse da resposta, pro padrão já decodificar os dados pra utf-8
    JSON também é suportado"""

    def get_data(self):
        return Response.get_data(self, True)

    def get_json(self):
        if self.content_type == 'application/json':
            return json.loads(self.get_data())
