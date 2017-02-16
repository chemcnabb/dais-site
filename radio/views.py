from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class RadioView(TemplateView):
    template_name = "radio.html"