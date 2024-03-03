from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    from . import weather
    app.register_blueprint(weather.bp)
    return app
