from flask import Flask

import os


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = os.path.join(app.root_path, '..', 'config', 'production.cfg')
    else:
        config = os.path.join(app.root_path, '..', 'config', config)

    app.config.from_pyfile(config)

    from rest import restv1
    restv1.init_app(app)
    
    return app
