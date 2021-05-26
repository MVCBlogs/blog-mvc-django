from django.contrib import admin
from blog.Models.Post import Post
from blog.Models.Comment import Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
