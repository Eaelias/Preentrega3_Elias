from django.contrib import admin
from AppBlog.models import Author, Reader, Post, Contact

admin.site.register(Author)
admin.site.register(Reader)
admin.site.register(Post)
admin.site.register(Contact)