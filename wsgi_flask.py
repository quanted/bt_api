from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.serving import run_simple
import logging
import os
import bt_flask

app = DispatcherMiddleware(bt_flask.app)

if __name__ == "__main__":
    run_simple('localhost', 3345, app, use_reloader=True, use_debugger=True, use_evalex=True)