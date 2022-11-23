from flask import Flask
import os

def create_app():
    app=Flask(__name__)

    # añadimos variables de entorno a la app
    app.config.from_mapping(
        SENDGRID_KEY=os.environ.get('SENDGRID_KEY')
    )

    # importamos la aplicación
    from . import portfolio
    # registramos blueprint
    app.register_blueprint(portfolio.bp)

    return app