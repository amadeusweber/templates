# Config
import configparser
config = configparser.RawConfigParser()
config.read('app.conf')

# Logging
import logging
logging.basicConfig(
    **config['Logging']
)
logger = logging.getLogger(__name__)

# Flask App
import flask
from flask_cors import CORS
app = flask.Flask(__name__)
CORS(app)

# Modules
import modules.example.api as example
app.register_blueprint(example.api, url_prefix=f"/api/v{example.__version__}/example")

# Start app
if __name__ == '__main__':
    logger.info('Launching app')
    app.run(
        **config['Serve'],
    )