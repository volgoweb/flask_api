# -*- coding: utf-8 -*-
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SECRET_KEY = 'a_dfWj23Fl-qAf$ja'

# DATABASE = '/flask_api.db'
# USERNAME = 'volgoweb'
# PASSWORD = 'volgoweb'

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'db_repository')