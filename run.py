# -*- coding: utf-8 -*-
from app import app

app.run(debug=app.config.get('DEBUG', False))