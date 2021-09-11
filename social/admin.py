from django.contrib import admin
from .models import Post, Profile, Relationship, Url

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Url)
admin.site.register(Relationship)