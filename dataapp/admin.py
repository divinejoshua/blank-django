from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import NameList, Visitors, NameListCheck


admin.site.register(NameList)
admin.site.register(Visitors)
admin.site.register(NameListCheck)