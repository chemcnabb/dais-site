from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from about.models import AboutPage


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        page = AboutPage.objects.first()
        context['page'] = page
        return context