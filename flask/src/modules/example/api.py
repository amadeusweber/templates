# Version
__version__ = '1'

# Imports

# Logging
import logging
logger = logging.getLogger(__name__)

# Api
import flask
api = flask.Blueprint('example', __name__)

@api.route('/')
def index():
    return flask.send_file('html/index.html')