from . import db
from sqlalchemy.sql import func 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager



class Pitches(db.Model):
    __tablename__='pitches'

    id = db.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    pitcher = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)
    comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
    upvotes = db.relationship('Upvote', backref = 'pitch', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'pitch', lazy = 'dynamic')

    @classmethod
    def get_pitches(cls, id):
        pitches = Pitches.query.order_by(pitch_id=id).desc().all()
        return pitches

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'Pitch {self.description}'



class Comment(db.Model):
    __tablename_='comments'
    id = db.Column(db.Integer, primarykey = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id)
        return comments

    def __repr__(self):
        return f'Comments: {self.comment}'
    





class User(UserMixin, db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    about = db.Column(db.String(255))
    avatar = db.Column(db.String())
    password_encrypt=db.Column(db.String(128))
    pitches = db.relationship('Pitches', backref='user', lazy='dynamic')
    likes = db.relationship('UpVote', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='comments', lazy='dynamic')


    @property

    def password(self):
        raise AttributeError('You cannot read the password attribute') 
    @password.setter

    def password(self, password):
        self.password_encrypt = generate_password_hash(password)
     
    def check_password(self, password):
         return check_password_hash(self.password_encrypt, password )
    
    
    def __repr__(self):
        return f'User{self.username}'
    
    


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User', backref = 'role', lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name} '
        