from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
import re

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100, message="Name must be between 2 and 100 characters")
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Please enter a valid email address"),
        Length(max=100)
    ])
    subject = StringField('Subject', validators=[
        DataRequired(),
        Length(min=3, max=200, message="Subject must be between 3 and 200 characters")
    ])
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=1000, message="Message must be between 10 and 1000 characters")
    ])
    submit = SubmitField('Send Message')

    def validate_message(self, field):
        # Check for spam patterns
        spam_patterns = [
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            r'\b(buy|sell|cheap|free|money|cash|loan|investment)\b',
        ]
        
        for pattern in spam_patterns:
            if re.search(pattern, field.data, re.IGNORECASE):
                raise ValidationError('Message contains prohibited content.')

class NewsletterForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Email(message="Please enter a valid email address"),
        Length(max=100)
    ])
    submit = SubmitField('Subscribe')
