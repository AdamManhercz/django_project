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
            "maxlenght":"16",
            "minlenght":"6"
        })
        self.fields["email"].widget.attrs.update({
            "required":"",
            "name":"email",
            "id":"email",
            "type":"email",
            "placeholder":"E-mail",
            "maxlenght":"16",
            "minlenght":"6"
        })
        self.fields["password1"].widget.attrs.update({
            "required":"",
            "name":"password1",
            "id":"password1",
            "type":"password",
            "placeholder":"Password",
            "maxlenght":"16",
            "minlenght":"6"
        })
        self.fields["password2"].widget.attrs.update({
            "required":"",
            "name":"password2",
            "id":"password2",
            "type":"password",
            "placeholder":"Password again",
            "maxlenght":"16",
            "minlenght":"6"
        })


    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']