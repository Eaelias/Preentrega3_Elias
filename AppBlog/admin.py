from django.contrib import admin
from AppBlog.models import Post, Contact, Category, Comment
from accounts.models import Profile

admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)