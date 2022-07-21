from django.contrib import admin
from .models import Category, Post, Postman, Publisher

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Postman)
admin.site.register(Publisher)