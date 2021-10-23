from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Url, Profile

MODO = (
    ('Business', 'Business'),
    ('Social', 'Social'),
    ('Otro', 'Otro')
)

COLOR = (
    ('fucsia', 'Fucsia'),
    ('blanco', 'Blanco'),
    ('negro', 'Negro'),
    ('rojo', 'Rojo'),
    ('azul', 'Azul'),
    ('verde', 'Verde'),
    ('amarillo', 'Amarillo'),
    ('naranja', 'Naranja'),
    ('gris', 'Gris'),
    ('violeta', 'Violeta')
)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirma Contraseña',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: "" for k in fields}


class PostForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows': 2, 'placeholder': '¿Qué está pasando?'}),
                              required=True)

    class Meta:
        model = Post
        fields = ['content']


class UrlForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={'rows': 2, 'placeholder': 'Añade el nombre del boton', 'class': 'form-control'}), required=True)
    content = forms.CharField(label='', widget=forms.TextInput(
        attrs={'rows': 2, 'placeholder': 'Añade una Url (Instagram,facebook,etc.)', 'class': 'form-control'}),
                              required=False)
    archivo = forms.FileField(label='o añade un archivo pdf', required=False)
    modo = forms.ChoiceField(label='Seleccione un modo', widget=forms.Select(attrs={'rows': 2, 'class': 'form-select'}),
                             choices=MODO)

    class Meta:
        model = Url
        fields = ['title', 'content', 'archivo', 'modo']


class EditProfileForm(forms.ModelForm):
    imageB = forms.ImageField(label='Seleccione una foto de perfil',
                             widget=forms.FileInput(attrs={'rows': 2, 'class': 'form-control'}), required=False)
    imageS = forms.ImageField(label='',
                             widget=forms.FileInput(attrs={'rows': 2, 'class': 'form-control'}), required=False)
    imageO = forms.ImageField(label='',
                              widget=forms.FileInput(attrs={'rows': 2, 'class': 'form-control'}), required=False)
    portadaB = forms.ImageField(label='Seleccione una foto de portada',
                               widget=forms.FileInput(attrs={'rows': 2, 'class': 'form-control'}), required=False)
    portadaS = forms.ImageField(label='',
                                widget=forms.FileInput(attrs={'rows': 2, 'class': 'form-control'}), required=False)
    portadaO = forms.ImageField(label='',
                                widget=forms.FileInput(attrs={'rows': 2, 'class': 'form-control'}), required=False)
    modo = forms.ChoiceField(label='Seleccione un modo', widget=forms.Select(attrs={'rows': 2, 'class': 'form-select'}),
                             choices=MODO)
    colorBoton = forms.ChoiceField(label='Seleccione Color para los botones/links',
                                   widget=forms.Select(attrs={'rows': 2, 'class': 'form-select'}), choices=COLOR)
    colorFondo = forms.ChoiceField(label='Seleccione Color para el fondo',
                                   widget=forms.Select(attrs={'rows': 2, 'class': 'form-select'}), choices=COLOR)

    class Meta:
        model = Profile
        fields = ['imageB', 'imageS', 'imageO', 'portadaB', 'portadaS', 'portadaO', 'modo', 'colorBoton', 'colorFondo']


class ModoProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        # fields = ['modo']
        fields = '__all__'
    # hidden = ['user', 'image', 'colorBoton', 'colorFondo']
