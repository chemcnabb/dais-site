from django.contrib import admin
from team.models import TeamMember

class TeamAdmin(admin.ModelAdmin):
    save_as = True

admin.site.register(TeamMember, TeamAdmin)
