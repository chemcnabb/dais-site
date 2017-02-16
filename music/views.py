from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class MusicView(TemplateView):
    template_name = "music.html"