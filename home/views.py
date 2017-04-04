from django.shortcuts import render
from django.views.generic import TemplateView
from watch.models import WatchPost
from look.models import LookPost
from listen.models import ListenPost
# Create your views here.
from itertools import chain

class HomeView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # context["post_list"] = list(chain(WatchPost.objects.all(),LookPost.objects.all(), ListenPost.objects.all()))
        context["post_list"] = sorted(
            chain(WatchPost.objects.exclude(poster_image__isnull=True).exclude(poster_image__exact='').all(), LookPost.objects.exclude(poster_image__isnull=True).exclude(poster_image__exact='').all(), ListenPost.objects.exclude(poster_image__isnull=True).exclude(poster_image__exact='').all()),
            key=lambda instance: instance.order, reverse=False
        )
        # context["post_list"].reverse()
        context["row_count"] = 0

        return context