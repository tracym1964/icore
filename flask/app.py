import logging
import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
from uploads.views import uploads
from database import MysqlSession

app = Flask(__name__)

# Register additional packages
app.register_blueprint(uploads)

CORS(app)

# Globals
UPLOAD_FOLDER = '/temp_files/'
ALLOWED_EXTENSIONS = set(['xlsx', 'xls'])

# Application-level logging
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)


@app.teardown_appcontext
def shutdown_session(exception=None):
    MysqlSession.remove()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
@app.route('/healthz')
def root():
    return 'OK', 200


@app.route('/test/test', methods=['POST'])
def upload_file():
    app.logger.info('Message Received')
    error = None
    # schema = TestApi()
    if 'files' not in request.files:
        app.logger.info(request.files)
        return 'Error No Files', 500

    file = request.files['files']

    if file and allowed_file(file.filename):
        # Move this to where ever you like
        file.save(file.filename)
        return 'OK', 200

    return 'Something is Wrong', 500


if __name__ == '__main__':
    app.run()

