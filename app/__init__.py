import os

from flask import Flask, redirect, request
from werkzeug.middleware.proxy_fix import ProxyFix

from app.content import portfolio_data


def create_app():
    app = Flask(__name__)

    # Basic Config — SECRET_KEY from env so production can override without a code change.
    # Fallback keeps the app starting if PythonAnywhere has not set the variable yet.
    app.secret_key = os.environ.get('SECRET_KEY', 'dev-key-please-change')
    app.config['ENABLE_RESUME_DOWNLOAD'] = True

    # PythonAnywhere terminates TLS at the proxy and forwards HTTP internally.
    app.wsgi_app = ProxyFix(app.wsgi_app, x_proto=1, x_host=1)

    @app.before_request
    def redirect_http_to_https():
        host = (request.host or '').split(':')[0]
        if host in ('localhost', '127.0.0.1'):
            return None
        if request.is_secure:
            return None
        url = request.url.replace('http://', 'https://', 1)
        return redirect(url, code=301)

    # Context Processor to inject portfolio data into all templates
    @app.context_processor
    def inject_portfolio_data():
        return dict(item=portfolio_data)

    # Register Blueprints
    from app.blueprints.main.routes import main
    app.register_blueprint(main)

    return app
