from django.contrib import admin

# Register your models here.
from .models import NameList, BlogPost


admin.site.register(NameList)
admin.site.register(BlogPost)
