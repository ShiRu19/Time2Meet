from django.contrib import admin
from .models import User, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectName')
    search_fields = ('id','projectName')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'userName', 'userPassword')
    search_fields = ('id','userName')

admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)