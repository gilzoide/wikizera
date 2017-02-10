# -*- coding: utf-8 -*-

WIKIZERA_REACT_ORIGIN = 'http://localhost:3000'

MONGODB_DB = 'sessoes-testdb'
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

SECRET_KEY = 'minha eguinha pocoto - teste'
SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
SECURITY_PASSWORD_SALT = SECRET_KEY
SECURITY_TOKEN_AUTHENTICATION_KEY = 'authtoken'
SECURITY_REGISTERABLE = True
# pra rolar login por json
WTF_CSRF_ENABLED = False

# admin mais facil, tirar no produção
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
SECURITY_CHANGEABLE = True

TESTING = True
