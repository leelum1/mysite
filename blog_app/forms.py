from django import forms
from .models import Post, BlogImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'keywords', 'cover']
        labels = {
            'title': 'Title',
            'text': 'Text',
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = BlogImage
        fields = ['image', 'caption', 'is_main',]
        # labels = {
        #     'title': 'Title',
        #     'text': 'Text',
        # }
