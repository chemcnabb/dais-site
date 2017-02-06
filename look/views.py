from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class LookView(TemplateView):
    template_name = "look.html"