from app import db


class Student(db.Model):
    __tablename__ = 'students_table'

    name = db.Column(db.String())
    address = db.Column(db.String())
    gender = db.Column(db.String())
    last_name = db.Column(db.String())
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name='', address='', gender='', last_name=''):
        self.name = name
        self.address = address
        self.gender = gender
        self.last_name = last_name

    def __repr__(self):
        return '<name {}>'.format(self.name)

