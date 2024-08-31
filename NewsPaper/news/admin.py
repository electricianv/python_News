from django.contrib import admin
from .models import Category, Post # Импортируйте вашу модель Category

admin.site.register(Category)
admin.site.register(Post)