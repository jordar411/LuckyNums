from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import NumberRange, InputRequired, Email


class AddUserForm(FlaskForm):

    name = StringField("User Name", validators=[InputRequired(message="User name can't be blank.")])
    email = StringField("Email", validators=[InputRequired(message="Email can't be blank."), Email()])
    year = IntegerField("Birth Year", validators=[InputRequired(message="Birth year can't be blank."), NumberRange(min=1900, max=2020, message="Birth year must be between %(min)s and %(max)s.")])
    color = SelectField("Color", validators=[InputRequired(message="Color can't be blank.")], choices=[(
        'red', 'red'), ('green', 'green'), ('orange', "orange"), ('blue', "blue")])