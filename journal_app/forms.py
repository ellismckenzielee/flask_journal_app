from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(), Length(min=2, max=20)])
    content = StringField('content', validators=[DataRequired()])
    submit = SubmitField('Submit')