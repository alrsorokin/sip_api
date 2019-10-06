from sip_api.app import db

from . import Base


class Operator(Base):
    __tablename__ = 'operator'

    phone_number = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
