from django.contrib import admin
from .models import User, Project, Participation, ParticipationDetail

class ParticipationInline(admin.TabularInline):
    model = ParticipationDetail

class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ParticipationInline
    ]
    list_display = ('id', 'projectName', 'availableTime')
    search_fields = ('id','projectName', 'availableTime')

class UserAdmin(admin.ModelAdmin):
    inlines = [
        ParticipationInline
    ]
    list_display = ('id', 'userName', 'userPassword', 'availableTime')
    search_fields = ('id','userName', 'availableTime')

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectId', 'userId')
    search_fields = ('id','projectId', 'userId')

admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Participation, ParticipationAdmin)