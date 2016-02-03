# -*- coding: utf-8 -*-
from app import app
from flask import render_template, request

@app.route('/')
def front_page():
    context = {
        'count_news': 3,
    }
    dir_req = dir(request)
    app.logger.debug('debug message')
    app.logger.debug(dir_req)
    return render_template("front.html", **context)

@app.route('/page/<int:page_id>')
def contacts_page(page_id):
    return u'Is page №%d' % page_id