from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class TeamView(TemplateView):
    template_name = "team.html"