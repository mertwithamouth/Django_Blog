from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.caption



class Post(models.Model):
    title = models.CharField(max_length=200)
    author=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    excerpt = models.CharField(max_length=200)
    image=models.ImageField(upload_to='posts/',null=True)
    date = models.DateField(auto_now=True)
    slug=models.SlugField(default = '', null=False, db_index=True, blank=True)
    tag=models.ManyToManyField(Tag)
    content = models.TextField()
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])


    def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.slug])

    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.CASCADE)
    text=models.TextField(max_length=400)
    post=models.ForeignKey(Post,on_delete=models.SET_NULL, null=True, related_name='comments')


class StoredPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)