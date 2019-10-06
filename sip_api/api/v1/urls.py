from flask import abort, jsonify, make_response, request

from sip_api.app import app
from sip_api.lib import const as c
from sip_api.lib.helper import hash_password, generate_token
from sip_api.models import User

from .call import CallListView
from .operator import OperatorListView
from .recording import RecordingView


@app.route('/api/v1/health-check', methods=['GET'])
def health_check():
    from sip_api.models import Operator
    Operator.query.first()
    return 'OK'


@app.route('/users', methods=['GET'])
def new_user():
    auth = request.authorization

    if auth and auth.username and auth.password:
        login = auth.username
        password = auth.password

        user = User.query.filter_by(login=login).first()
        if not user:
            user = User(login=login,
                        password=hash_password(password),
                        token=generate_token()).save()
        return make_response(jsonify({'token': user.token}), 200)

    return make_response(c.ERRORS[401], 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})


app.add_url_rule('/api/v1/calls', view_func=CallListView.as_view('call'))
app.add_url_rule('/api/v1/operators', view_func=OperatorListView.as_view('operator'))
app.add_url_rule('/api/v1/recording', view_func=RecordingView.as_view('recording'))
