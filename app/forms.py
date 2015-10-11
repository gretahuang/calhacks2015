from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

# class LandlordForm(Form):
#     name = StringField('Name', 
#                        validators=[Required(message='Your name is required.'),
#                        Length(1, 64)])
#     website = StringField('Website', validators=[URL(), Optional()])
#     description = TextAreaField('Description')   
#     submit = SubmitField('Update profile')

class SearchForm(Form):
    query = StringField('Search', validators=[Required()])
    submit = SubmitField('Submit')

# class ReviewForm(Form):
#     query = StringField('Query', validators=[Required()])
#     submit = SubmitField('Submit')