from django.shortcuts import render
from django.views.generic import TemplateView
from team.models import TeamMember
# Create your views here.


class TeamView(TemplateView):
    template_name = "team.html"
    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)

        context["team_members"] = TeamMember.objects.all()


        return context