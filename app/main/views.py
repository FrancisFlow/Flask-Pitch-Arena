from flask import render_template, redirect, url_for
from . import main
from ..models import Comment, Downvote, Pitches, Upvote, User

from flask_login import login_required, current_user
from .forms import CommentForm, UpdateProfile, AddPitch, UpvoteForm, DownvoteForm
from .. import db
from flask.views import View, MethodView

Comment = Comment.comment

@main.route('/')
def index():

    title = "Pitch Arena"
    return render_template('home.html', title =title)




# @main.route('/user/<name>/update', methods= ['GET', 'POST'])
# @login_required
# def update_profile(name):
#     user = User.query.filter_by(username=name).first()
#     if user is None:
#         abort(404)

#     form = UpdateProfile()

#     if form.validate_on_submit():
#         user.description = form.description.data

#         return redirect(url_for('.profile', name = user.username))




@main.route('/comment/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()

    pitch = Pitches.query.get(pitch_id)


    if form.validate_on_submit():
        description = form.description.data
        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('.new_comment', pitch_id = pitch.id))
    
    all_comments = Comment.query.filter_by( pitch_id = pitch_id).all()
    return render_template('new_comment.html', form = form, comment= all_comments, pitch = pitch)


@main.route('/pitches/new', methods = ['GET', 'POST'])
def new_pitch():
    form = AddPitch()

    my_upvotes = Upvote.query.filter_by(pitch_id=Pitches.id)
    if form.validate_on_submit():
        pitcher = form.pitcher.data
        description = form.description.data
        title= form.title.data
        owner_id =current_user
        category = form.category.data

        new_pitch= Pitches(owner_id= current_user._get_current_object().id, title=title, description=description, category=category, pitcher=pitcher)
        db.session.add(new_pitch)
        db.session.commit()

        return redirect(url_for('main.categories'))
    return render_template('new_pitch.html', form=form)

@main.route('/categories')
def categories():

    title = 'Pitches | Categories'
    pitch=Pitches.query.filter_by().first()
    Business = Pitches.query.filter_by(category="Business")
    Pick_up_lines= Pitches.query.filter_by(category="Pick_up_lines")
    Self_Pitch = Pitches.query.filter_by(category= "Self-Pitch")
    Sales_Pitch= Pitches.query.filter_by(category= "Sales_Pitch")
    upvotes = Upvote.get_all_upvotes(Pitch_id=Pitches.id)
    downvotes = Downvote.get_all_downvotes(pitch_id=Pitches.id)

    return render_template('categories.html', title=title, pitch =pitch, Business = Business, Pick_up_lines=Pick_up_lines, Self_Pitch=Self_Pitch, Sales_Pitch=Sales_Pitch, upvotes=upvotes, downvotes=downvotes)

@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
def upvote(pitch_id):
    pitch = Pitches.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id = pitch_id)

    if Upvote.query.filter_by(Upvote.user_id==user.id, Upvote.pitch_id==pitch_id).first():
        return redirect(url_for('main.categories'))

    new_upvote = Upvote(pitch_id = pitch_id, user =current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.categories'))


@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
def downvote(pitch_id):
    pitch= Pitches.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id=pitch_id)

    if Downvote.query.filter(Downvote.user_id == user.id, Downvote.pitch_id == pitch_id).first():
        return redirect(url_for('main.categories'))

    new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.categories'))