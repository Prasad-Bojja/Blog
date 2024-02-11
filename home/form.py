from django import forms
from tinymce.widgets import TinyMCE
from .models import BlogModel

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = ['title', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': TinyMCE(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
