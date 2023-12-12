from django.contrib import admin
from AppBlog.models import Post, Contact, Category, Comment

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Comment)