from sqlalchemy.exc import DatabaseError

from sip_api.app import db


class Manager():
    def __init__(self, model):
        self.model = model

    @property
    def query(self):
        return self.model.query


class Base(db.Model):
    __abstract__ = True
    __manager__ = Manager

    class ManagerDescriptor(object):
        def __get__(self, instance, model):
            return model.__manager__(model)

    objects = ManagerDescriptor()

    def save(self):
        db.session.add(self)
        self._flush()
        return self

    def update(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return self.save()

    def delete(self):
        db.session.delete(self)
        self._flush()

    @staticmethod
    def _flush():
        try:
            db.session.flush()
        except DatabaseError:
            db.session.rollback()
            raise
