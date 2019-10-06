from sip_api.app import ma
from sip_api.models import Operator


class OperatorSchema(ma.ModelSchema):
    class Meta:
        model = Operator
