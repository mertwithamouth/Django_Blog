from django.contrib import admin
from .models import Post,Tag,Author,Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter  = ('tag','author','date')
    list_display = ('title','author','date')
    prepopulated_fields = {'slug':('title',)}

class CommentAdmin(admin.ModelAdmin):

    list_display = ('user_name','text','post')


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment,CommentAdmin)