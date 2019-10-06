from flask import abort, make_response
from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from sip_api.app import token_auth
from sip_api.models import Operator

from .schema import OperatorSchema


class OperatorListView(MethodView):

    @token_auth.login_required
    def get(self):
        try:
            operators = Operator.query.all()
        except DatabaseError:
            abort(400)

        schema = OperatorSchema(many=True)
        return make_response({'operators': schema.dump(operators)})
