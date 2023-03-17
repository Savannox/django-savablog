from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre:', required=True, min_length=3, max_length=30, 
                           widget=forms.TextInput(attrs={'placeholder':'Escribe tu nombre', 'class':'controls'}))
    email = forms.EmailField(label='Email', required=True, min_length=3, max_length=30,
                             widget=forms.TextInput(attrs={'placeholder':'Escribe tu correo', 'class':'controls'}))
    message = forms.CharField(label='Contenido', required=True,
                              widget=forms.Textarea(attrs={'placeholder':'Escribe tu mensaje', 'class':'text-areas'}))