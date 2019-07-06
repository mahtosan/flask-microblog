from flask import request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField , SubmitField
from wtforms.validators import DataRequired, ValidationError, Length
from app.models import User




class EditProfileForm(FlaskForm):
    username = StringField('Kullanıcı adı: ', validators=[DataRequired()])
    about_me = TextAreaField('Hakkımda: ', validators=[Length(min=0,max=140)])
    submit = SubmitField('Kaydet')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Lütfen farklı bir kullanıcı adı seçin.')




class PostForm(FlaskForm):
    post = TextAreaField('Bir şeyler yaz', 
                validators=[DataRequired(), Length(min=1,max=140)])
    
    submit = SubmitField('Paylaş')




class SearchForm(FlaskForm):
    q = StringField('Ara', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        
        super(SearchForm,self).__init__(*args, **kwargs)