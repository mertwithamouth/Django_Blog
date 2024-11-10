from .models import Author
from django import forms
from .models import Post, Comment

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
