# -*- coding: utf-8 -*-

from core.database import db
from core.app import create_app
from flask_migrate import Migrate
from flask_migrate import MigrateCommand
from flask_script import Server, Manager

app = create_app()
migrate = Migrate(app, db)

manage = Manager(app)

if __name__ == "__main__":
    manage.add_command('runserver', Server)
    manage.add_command('db', MigrateCommand)
    manage.run()
