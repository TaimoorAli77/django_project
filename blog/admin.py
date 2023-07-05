from django.contrib import admin

# Register your models here.

from .models import Post

# to register

admin.site.register(Post)