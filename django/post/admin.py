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
    list_display = ('id', 'userName', 'userPassword')
    search_fields = ('id','userName')

class ParticipationAdmin(admin.ModelAdmin):
    list_display = ('id', 'projectId', 'userId', 'availableTime')
    search_fields = ('id','projectId', 'userId', 'availableTime')

admin.site.register(Project, ProjectAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Participation, ParticipationAdmin)