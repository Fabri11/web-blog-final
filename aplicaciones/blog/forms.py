
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1: forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label= 'Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        help_texts = {k:"" for k in fields}

class PostForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    descripcion = forms.TextInput()
    imagen = forms.ImageField()
    data = forms.DateField()