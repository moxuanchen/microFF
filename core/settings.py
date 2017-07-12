# -*- coding: utf-8 -*-

import os
import yaml


class Config(object):

    def __init__(self):

        yaml_file = os.path.join(os.path.dirname(__file__), self.__class__.__name__ + '.yml')

        if os.path.exists(yaml_file):
            with open(yaml_file, 'r') as fp:
                obj = yaml.load(fp.read()) or {}
                for key in obj.keys():
                    setattr(self, key, obj[key])


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'


class ProdConfig(Config):
    DEBUG = False


def get_config_env():
    if os.environ.get("CONFIG_ENV") == 'prod':
        return ProdConfig()
    return DevConfig()
