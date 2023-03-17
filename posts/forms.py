from django import forms
from posts.models import PostsModel

class PostForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'controls', 'placeholder':'Titulo'}))
    content = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'text-areas', 'placeholder':'Mensaje'}))
    
    class Meta:
        model = PostsModel
        fields = ['title', 'content', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class':'files'})
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label_suffix = ''