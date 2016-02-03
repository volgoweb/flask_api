# -*- coding: utf-8 -*-
import os.path
from migrate.versioning import api
from settings import SQLALCHEMY_DATABASE_URI
from settings import SQLALCHEMY_MIGRATE_REPO

from application import db


db.create_all()
if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
else:
    # print '--------------------- migrate.version'
    # print api.version(SQLALCHEMY_MIGRATE_REPO)
    #api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))