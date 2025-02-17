import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower (Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,  ForeignKey ('user.id'))
    user_to_id = Column(Integer,  ForeignKey ('user.id'))


class User (Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False)
    first_name = Column (String(30), nullable=False)
    last_name = Column (String(30), nullable=False)
    email = Column (String (50), nullable=False)


class Media (Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column (String (250), nullable=False)
    post_id = Column (Integer, ForeignKey ('post.id'))

class Post (Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column (Integer, ForeignKey ('user.id'))

class Likes (Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id')) 
    liked_by_followers = Column (Integer, ForeignKey ('follower.id'))


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer, ForeignKey ('user.id'))
    post_id = Column (Integer, ForeignKey ('post.id')) 

class Share (Base):
    __tablename__ = 'share'
    id = Column(Integer, primary_key=True) 
    post_id = Column (Integer, ForeignKey ('post.id')) 
    shared_by_follower = Column (Integer, ForeignKey ('follower.id'))

class Save (Base):
    __tablename__ = 'save'
    id = Column(Integer, primary_key=True)
    post_id = Column (Integer, ForeignKey ('post.id')) 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
