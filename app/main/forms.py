from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required




class AddPitch(FlaskForm):
    pitcher = StringField("Submitted By: Your Name ...", validators = [Required()])
    title = StringField("Pitch Title", validators = [Required()])
    category = SelectField("What category are you submitting to?", choices=[("Business", "Business"), ( "Pick-up-lines", "Pick_up_lines"), ("Self_Pitch", "Self_Pitch"), ("Sales_Pitch", "Sales_Pitch")],validators=[Required()])
    description = TextAreaField('What pitch do you want to share?',validators = [Required()] )
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
   bio = TextAreaField('Add or modify your bio', validators = [Required()])
   submit = SubmitField('Submit')


class CommentForm(FlaskForm):
   description = TextAreaField('Add a new comment', validators = [Required()])
   submit= SubmitField('Submit')


class UpvoteForm(FlaskForm):
   submit = SubmitField('Upvote')


class DownvoteForm(FlaskForm):
   submit = SubmitField('Downvote')

