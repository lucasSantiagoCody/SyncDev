from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'{field_name}...'
            if field_name == 'password1':
                field.widget.attrs['minlength'] = 8
            if field_name == 'email':
                field.widget.attrs['autofocus'] = False

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'username')

class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = f'{field_name}...'
            if field_name == 'email':
                field.widget.attrs['autofocus'] = True