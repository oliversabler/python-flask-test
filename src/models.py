from app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    created_date = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return '<id {}>'.format(self.id)