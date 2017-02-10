# -*- coding: utf-8 -*-

from flask_security import UserMixin, RoleMixin
from flask_security.utils import encrypt_password

from db import db


class Pagina(db.Document):
    """Página da wiki, em markdown"""
    name = db.StringField(unique=True)
    content = db.StringField()


class Role(db.Document, RoleMixin):
    """Grupo de permissões usado pelo flask-security"""
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    @classmethod
    def create_role(cls, name, description=None):
        return cls.objects.create(name=name, description=description)


class User(db.Document, UserMixin):
    """Usuário, seguro com senha, participante de Roles e talz"""
    username = db.StringField(max_length=255)
    email = db.EmailField(max_length=255, unique=True)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    roles = db.ListField(db.ReferenceField(Role, reverse_delete_rule=db.DENY), default=[])
    pages = db.ListField(db.ReferenceField(Pagina, reverse_delete_rule=db.NULLIFY), default=[])

    @classmethod
    def create_user(cls, email, password, username=None, roles=None, active=True):
        return cls(email=email, password=password, username=username, roles=roles, active=active)
