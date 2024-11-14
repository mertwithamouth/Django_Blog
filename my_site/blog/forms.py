from .models import Author
from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=['post']
        labels ={
            'user_name':'Your Name',
            'text':'Your Comment'
        }

