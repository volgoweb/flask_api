# -*- coding: utf-8 -*-
from application import app

app.run(debug=app.config.get('DEBUG', False))