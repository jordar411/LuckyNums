from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String, nullable=False)
    lucky_num = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<User #{self.id}: name={self.name} email={self.email} birth_year={self.birth_year} color={self.color} lucky_num={self.lucky_num}>'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birth_year': self.birth_year,
            'color': self.color,
            'lucky_num': self.lucky_num
        }