from app import Base
from sqlalchemy.orm import backref, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer)
    role = Column(String(50))
    is_admin = Column(Boolean)
    game = Column(Integer, ForeignKey('games.id'), nullable= True)

    def __repr__(self):
        return f'<User {self.user_id}>'

class Games(Base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key = True, autoincrement = True)
    creator_id = Column(Integer, ForeignKey('users.id'), nullable= False)
    created_at = Column(Integer)
    is_online = Column(Boolean)
    chat_id = Column(Integer)
    players = relationship(Users, foreign_keys = 'Users.game')

    def __repr__(self):
        return f'<Game {self.id}>'