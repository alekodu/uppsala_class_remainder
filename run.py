#!/usr/bin/python
from app import application

try:
    application.run(debug=True, threaded=True)
except Exception as e:
    print(e)
