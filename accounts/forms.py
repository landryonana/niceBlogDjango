from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from blog.models import Profile


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
            'tabindex': '1',
            'value': '',
            'placeholder': 'Username',
        }
    ))
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'tabindex': '2',
            'name': 'password',
            'value': '',
            'placeholder': 'Password',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
            'tabindex': '1',
            'placeholder': 'Username',
        }
    ))
    email = forms.CharField(max_length=250, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'name': 'email',
            'tabindex': '1',
            'placeholder': 'Email Address',
        }
    ))
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'first_name',
            'name': 'first_name',
            'tabindex': '1',
            'placeholder': 'First Name',
        }
    ))
    password = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'password',
            'tabindex': '2',
            'name': 'password',
            'placeholder': 'Password',
        }
    ))
    password2 = forms.CharField(max_length=250, widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'confirm-password',
            'tabindex': '2',
            'name': 'confirm-password',
            'placeholder': 'Confirm Password',
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'username',
            'name': 'username',
            'tabindex': '1',
            'placeholder': 'Username',
        }
    ))
    first_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'first_name',
            'name': 'first_name',
            'tabindex': '1',
            'placeholder': 'First Name',
        }
    ))
    last_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'last_name',
            'name': 'last_name',
            'tabindex': '1',
            'placeholder': 'Last Name',
        }
    ))
    email = forms.CharField(max_length=250, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'id': 'email',
            'name': 'email',
            'tabindex': '1',
            'placeholder': 'Email Address',
        }
    ))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'date_of_birth',
            'name': 'date_of_birth',
            'tabindex': '1',
            'placeholder': 'Date Of Birth',
        }
    ))
    photo = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'photo',
            'name': 'photo',
            'tabindex': '1',
            'placeholder': 'photo',
        }
    ))

    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']
