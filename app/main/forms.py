from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import Required

class CommentForm(FlaskForm):

   comment= TextAreaField('Make a comment', validators=[Required()])
   submit = SubmitField('Comment')



class AddPitch(FlaskForm):
    pitcher = StringField("Submitted By: Your Name ...", validators = [Required()])
    title = StringField("Pitch Title", validators = [Required()])
    category = SelectField("What category are you submitting to?", choices=[("twitter", "Twitter"), ( "elevator", "Elevator"), ("competition", "Competition"), ("investor", "Investor")],validators=[Required()])
    description = TextAreaField('What pitch do you want to share?',validators = [Required()] )
    submit = SubmitField('Submit')