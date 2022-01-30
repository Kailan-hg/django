from django import forms
from .models import Post

class Post_form(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','text',)
