from django.contrib import admin
from team.models import TeamMember

class TeamAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('full_name',)

admin.site.register(TeamMember, TeamAdmin)
