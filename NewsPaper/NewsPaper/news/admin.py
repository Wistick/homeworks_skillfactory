from django.contrib import admin
from .models import Author, Post, PostCategory, Comment

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
