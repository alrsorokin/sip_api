import time

from datetime import datetime

from flask import jsonify, make_response, request
from flask.views import MethodView

from sip_api.app import token_auth
from sip_api.models import Call

from .schema import CallSchema


class CallListView(MethodView):

    @token_auth.login_required
    def get(self):
        schema = CallSchema(many=True)
        today = datetime.now().replace(hour=0, second=0, microsecond=0)

        date_from = int(request.args.get('date_from', time.mktime(today.timetuple())))
        date_till = int(request.args.get('date_till',
                                         time.mktime(today.replace(hour=23).timetuple())))

        calls = (Call.query.filter(Call.date >= date_from)
                           .filter(Call.date <= date_till)
                           .all())
        resp = {
            'calls': schema.dump(calls)
        }
        return make_response(resp)
