from django.contrib import admin
from .models import News, Folder, Folder_News

# Register your models here.

admin.site.register(News)
admin.site.register(Folder)
admin.site.register(Folder_News)