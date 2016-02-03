# -*- coding: utf-8 -*-
from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    desc = db.Column(db.Text)

    def __repr__(self):
        return u'#{id} {title}'.format(id=self.id, title=self.title)