import yadisk

from flask import Flask, g, jsonify, make_response
from flask_httpauth import HTTPTokenAuth
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import DatabaseError

from sip_api.lib import const as c


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

disk = yadisk.YaDisk(token=app.config['YANDEX_TOKEN'])
token_auth = HTTPTokenAuth()


@app.after_request
def session_commit(response):
    try:
        db.session.commit()
    except DatabaseError:
        db.session.rollback()
        db.session.remove()
        raise

    return response


from sip_api import models  # isort:skip
from sip_api.api.v1 import urls  # isort:skip


@token_auth.verify_token
def verify_token(token):
    from sip_api.models import User
    g.current_user = User.objects.get_by_token(token) if token else None
    return g.current_user is not None


@token_auth.error_handler
def basic_auth_error():
    return make_response(jsonify(c.ERRORS[401]), 401)


@app.errorhandler(404)
def error_404(error):
    return make_response(jsonify(c.ERRORS[404]), 404)


@app.errorhandler(400)
def error_400(error):
    return make_response(jsonify(c.ERRORS[400]), 400)
