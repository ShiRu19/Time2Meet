from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectName', 'userName')
    search_fields = ('projectName', 'userName')

admin.site.register(Post, PostAdmin)