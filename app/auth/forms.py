from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Kullanıcı adı', validators=[DataRequired()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    remember_me = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')


class RegistrationForm(FlaskForm):
    username = StringField('Kullanıcı adı', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Şifre', validators=[DataRequired()])
    password2 = PasswordField('Şifrenizi Tekrar Girin', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Kayıt ol')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Kullanıcı adı kullanılmakta! Lütfen farklı bir kullanıcı adı girin')
        
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Girdiğiniz email adresi kullanılmakta! Lütfen farklı bir email adresi kullanın')






class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Şifremi sıfırla')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Yeni şifre', validators=[DataRequired()])
    password2 = PasswordField('Yeni şifrenizi tekrar girin', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Şifreni sıfırla')

