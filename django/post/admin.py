from django.contrib import admin
from .models import User, Project, Participation

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectName')
    search_fields = ('id','projectName')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'userName', 'userPassword')
    search_fields = ('id','userName')

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectId', 'userId')
    search_fields = ('projectId', 'userId')

admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Participation, ParticipationAdmin)