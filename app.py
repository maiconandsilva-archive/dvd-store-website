# THIRD PARTY IMPORTS
from flask import Flask
from werkzeug.utils import import_string
import os
import sys

# LOCAL IMPORTS
if os.getcwd() not in sys.path:
    # For flask run
    sys.path.insert(0, os.getcwd())
    
import server
import extensions as exts


def init_with(app):
    """Initialize extensions and funcions with the FLask"""
    on_production_env = app.config.get('FLASK_ENV') == 'production'
    
    exts.db.init_app(app)
    exts.talisman.init_app(app,
        force_https=on_production_env,
        force_https_permanent=on_production_env,
        content_security_policy=app.config['CSP'],
    )
    
    exts.create_tables(app)
    
    # The debugger should be the last to be initialized
    exts.init_debugger(app)
    
    
    
    
def create_app(pyconfig=None):
    app = Flask(__name__)
    
    # Flask Settings    
    cfg = import_string(os.getenv('FLASK_APPSETTINGS'))()
    app.config.from_object(cfg)
    
    if pyconfig:
        app.config.from_pyfile(pyconfig)
    
    # Register all blueprints
    # All blueprints will be imported from the server.py file
    app.register_blueprint(server.app)
    
    # Flask Extensions
    init_with(app)
    
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))    
