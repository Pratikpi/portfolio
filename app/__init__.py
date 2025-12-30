from flask import Flask

from app.content import portfolio_data

def create_app():
    app = Flask(__name__)
    
    # Basic Config
    app.secret_key = 'dev-key-please-change'
    app.config['ENABLE_RESUME_DOWNLOAD'] = True
    
    # Context Processor to inject portfolio data into all templates
    @app.context_processor
    def inject_portfolio_data():
        return dict(item=portfolio_data)

    # Register Blueprints
    from app.blueprints.main.routes import main
    app.register_blueprint(main)

    return app
