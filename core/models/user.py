# -*- coding: utf-8 -*-

from core.database import db
from core.database import Model
from core.database import SurrogatePK


class User(SurrogatePK, Model):

    __tablename__ = 'user'
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
