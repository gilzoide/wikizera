# -*- coding: utf-8 -*-

from wikizera.app import create_app

import json

"""The test application to use across all tests, it's always the same =]"""
test_app = create_app('test').test_client()

def _post_json(self, *args, **kwargs):
    kwargs['content_type'] = 'application/json'
    kwargs['data'] = json.dumps(kwargs['data'])
    return self.post(*args, **kwargs)

test_app.__class__.json = _post_json
