from django.contrib import admin
from .models import Author, Image, HastTag

# Register your models here.
admin.site.register(Author)
admin.site.register(Image)
admin.site.register(HastTag)
