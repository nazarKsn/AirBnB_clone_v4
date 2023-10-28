#!/usr/bin/python3
"""Flask Application"""
from flask import Flask
from models import storage
from os import environ
from api.v1.views import app_views
from flasgger import Swagger
from flasgger.utils import swag_from

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_db(error):
    """Close storage"""
    storage.close()


app.config['SWAGGER'] = {
        'title': 'AirBnB clone Restful API',
        'uiversion': 3
        }
Swagger(app)

if __name__ == "__main__":
    """Main function"""
    host = environ.get('HBNB_API_HOST', '0.0.0.0')
    port = environ.get('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
