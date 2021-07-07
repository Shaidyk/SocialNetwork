from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from SocialNetwork.models.profile import Profile
from SocialNetwork.models.photo import Photo


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50, required=False)
    nick = forms.CharField(max_length=50, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'nick',
            'email',
            'password1',
            'password2',
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
        )


class UploadForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea)
    is_avatar = forms.BooleanField()

    class Meta:
        model = Profile
        fields = (
            'title',
            'image',
            'description',
            'is_avatar',
        )

