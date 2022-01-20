from . import db
from sqlalchemy.sql import func 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.Query.get(int(user_id))

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
    id = db.Column(db.Integer, primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment = db.Column(db.String(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    
    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id)
        return comments

    @classmethod
    def get_comment_writer(cls, user_id):
        writer = User.query.filter_by(id=user_id).first()

        return writer

    def __repr__(self):
        return f'Comments: {self.comment}'
    





class User(UserMixin, db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(255))
    profile_pic_path=db.Column(db.String())
    pass_secure= db.Column(db.String(255))
    comment = db.relationship('Comment', backref = 'users', lazy = 'dynamic')
    pitch= db.relationship('Pitches', backref='users', lazy='dynamic')
    upvotes = db.relationship('Upvote', backref = 'users', lazy = 'dynamic')
    downvotes = db.relationship('Downvote', backref = 'users', lazy = 'dynamic')

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
    
    


# class Role(db.Model):
#     __tablename__ = 'roles'

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(255))
#     users = db.relationship('User', backref = 'role', lazy = "dynamic")

#     def __repr__(self):
#         return f'User {self.name} '

class Upvote(db.Model):
    __tablename__='upvotes'
    id = db.Column(db.Integer,primary_key=True)
    upvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_upvotes(self):
        db.session.add(self)
        db.session.commit()
    
    def add_upvotes(cls, id):

        upvote_pitch = Upvote(user = current_user, pitch_id=id)
        upvote_pitch.save_upvotes()

    @classmethod

    def get_upvotes(cls, id):
        upvote = Upvote.query.filter_by(pitch_id=id).all()
        return Upvote
    def __repr__(self):
        return f'{self.user_id}: {self.pitch_id}'



class Downvote(db.Model):
    __tablename__ = 'downvotes'

    id = db.Column(db.Integer,primary_key=True)
    downvote = db.Column(db.Integer,default=1)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_downvotes(self):
        db.session.add(self)
        db.session.commit()


    def add_downvotes(cls,id):
        downvote_pitch = Downvote(user = current_user, pitch_id=id)
        downvote_pitch.save_downvotes()

    
    @classmethod
    def get_downvotes(cls,id):
        downvote = Downvote.query.filter_by(pitch_id=id).all()
        return downvote

    @classmethod
    def get_all_downvotes(cls,pitch_id):
        downvote = Downvote.query.order_by('id').all()
        return downvote

    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'


    