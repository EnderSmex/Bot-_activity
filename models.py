from app import db
from sqlalchemy.orm import backref

class Users(db.Model):

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    user_id = db.Column(db.Integer)
    role = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean)
    game = db.Column(db.Integer, db.ForeignKey('games.id'), nullable= True)

    def __repr__(self):
        return f'<User {self.user_id}>'

class Games(db.Model):
    
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    created_at = db.Column(db.Integer)
    is_online = db.Column(db.Boolean)
    chat_id = db.Column(db.Integer)
    players = db.relationship(Users, foreign_keys = 'Users.game')

    def __repr__(self):
        return f'<Game {self.id}>'