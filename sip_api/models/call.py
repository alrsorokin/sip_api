from sip_api.app import db

from . import Base


class Call(Base):
    __tablename__ = 'call'

    id = db.Column(db.String, primary_key=True)
    type = db.Column(db.String, nullable=False)
    date = db.Column(db.Integer, nullable=False)
    duration_answer = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String, nullable=False)
    phone_number_client = db.Column(db.String, nullable=False)
    phone_number_operator = db.Column(db.String,
                                      db.ForeignKey('operator.phone_number'),
                                      nullable=False)

    hand_up_initiator = db.Column(db.String)
    transfers = db.Column(db.String)
    transfers_count = db.Column(db.Integer)
    holds_count = db.Column(db.Integer)
    holds_duration = db.Column(db.Integer)

    record_url = db.Column(db.String)
