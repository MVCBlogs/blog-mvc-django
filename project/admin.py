from django.contrib import admin
from project.Models.Post import Post
from project.Models.Comment import Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
