# -*- coding: utf-8 -*-
from flask import render_template, request, abort

from application import app, db
from models import Task


@app.errorhandler(404)
def page_not_found(error):
    return 'This page does not exist', 404


@app.route('/')
def front_page():
    context = {
        'count_news': 3,
        'tasks': Task.query.all()
    }
    app.logger.debug('debug message')
    return render_template("front.html", **context)


@app.route('/tasks/<int:id>')
def detail_task_page(id):
    t = Task.query.get(id)
    if not t:
        abort(404)
    context = {
        'task': t,
    }
    return render_template('task_detail_page.html', **context)