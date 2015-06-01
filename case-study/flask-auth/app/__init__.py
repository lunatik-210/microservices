from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

import os


db = SQLAlchemy()


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.path.join(app.root_path, '..', 'config', 'production.cfg')
    else:
        config = os.path.join(app.root_path, '..', 'config', config)

    app.config.from_pyfile(config)
    
    db.init_app(app)

    from rest import restv1
    restv1.init_app(app)

    from flask.ext.restful.representations.json import output_json
    output_json.func_globals['settings'] = {'ensure_ascii': False, 'encoding': 'utf8'}

    return app
