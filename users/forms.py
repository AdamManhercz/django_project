from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "required":"",
            "name":"username",
            "id":"username",
            "type":"text",
            "placeholder":"Username",
            "maxlength":"16",
            "minlength":"3"
        })
        self.fields["email"].widget.attrs.update({
            "required":"",
            "name":"email",
            "id":"email",
            "type":"email",
            "placeholder":"E-mail",
            "maxlength":"30",
            "minlength":"3"
        })
        self.fields["password1"].widget.attrs.update({
            "required":"",
            "name":"password1",
            "id":"password1",
            "type":"password",
            "placeholder":"Password",
            "maxlength":"16",
            "minlength":"3"
        })
        self.fields["password2"].widget.attrs.update({
            "required":"",
            "name":"password2",
            "id":"password2",
            "type":"password",
            "placeholder":"Password again",
            "maxlength":"16",
            "minlength":"3"
        })


    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']