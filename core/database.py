# -*- coding: utf-8 -*-

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class DBMixin:

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        db.session.add(instance)
        db.session.commit()


class Model(DBMixin, db.Model):
    __abstract__ = True


class SurrogatePK:

    id = db.Column(db.Integer, primary_key=True)
