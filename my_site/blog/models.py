from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from datetime import datetime

# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title = models.CharField(max_length=200)
    author=models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='posts')
    excerpt = models.CharField(max_length=200)
    image=models.ImageField(upload_to='posts/',null=True)
    date = models.DateField(auto_now=True)
    slug=models.SlugField(default = '', null=False, db_index=True, blank=True)
    tag=models.ManyToManyField(Tag)
    content = models.TextField()


    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])

class Comment(models.Model):
    user_name=models.CharField(max_length=30)
    text=models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.SET_NULL, null=True, related_name='comments')