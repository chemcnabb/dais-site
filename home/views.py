from django.shortcuts import render
from django.views.generic import TemplateView
from watch.models import WatchPost
from look.models import LookPost
from listen.models import ListenPost
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["post_list"] = [WatchPost.objects.all(),LookPost.objects.all(), ListenPost.objects.all()]


        return context