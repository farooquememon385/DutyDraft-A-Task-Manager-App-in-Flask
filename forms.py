from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()], render_kw={'placeholder':'Title'})
    dueDate = DateField('Due Date', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('submit')