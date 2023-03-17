from django import forms
from profiles.models import ProfileModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class':'controls', 'placeholder':'Nombre de usuario'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'controls', 'placeholder':'Correo electronico'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'controls', 'placeholder':'Contraseña'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'controls', 'placeholder':'Confirmar contraseña'}))
    photo = forms.ImageField(label='Foto de perfil', required=False, widget=forms.FileInput(attrs={'class':'files'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'photo']
        
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')      
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
    
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
            profile = ProfileModel.objects.create(user=user)
            if self.cleaned_data.get('photo'):
                profile.photo = self.cleaned_data.get('photo')
            else:
                profile.photo = 'users/pictures/user.png'
            profile.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ''
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario:', widget=forms.TextInput(attrs={'class':'controls'}))
    password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput(attrs={'class':'controls'}))