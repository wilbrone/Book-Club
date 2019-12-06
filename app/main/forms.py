from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, IMAGES

photo = UploadSet('photo', IMAGES)

class BookForm(FlaskForm):
    """docstring for BookForm."""

    title = StringField('Book title', validators = [Required()])
    author = StringField('Author', validators = [Required()])
    description = TextAreaField('Text', validators = [Required()])
