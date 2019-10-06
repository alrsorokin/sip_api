from sip_api.app import db

from . import Base, Manager


class UserManager(Manager):

    def get_by_token(self, token):
        return self.query.filter_by(login=token).first()


class User(Base):
    __tablename__ = 'user'
    __manager__ = UserManager

    login = db.Column(db.String, primary_key=True, unique=True)
    password = db.Column(db.String, nullable=False)

    token = db.Column(db.String, unique=True, nullable=False)
