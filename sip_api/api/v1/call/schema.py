from sip_api.app import ma
from sip_api.models import Call


class CallSchema(ma.ModelSchema):
    class Meta:
        model = Call
        include_fk = True
