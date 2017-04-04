from django.shortcuts import render
from django.views.generic import TemplateView
from music.models import MusicPost
# Create your views here.


class MusicView(TemplateView):
    template_name = "music.html"

    def get_context_data(self, **kwargs):
        context = super(MusicView, self).get_context_data(**kwargs)
        # context["post_list"] = list(chain(WatchPost.objects.all(),LookPost.objects.all(), ListenPost.objects.all()))

        context["post_list"] = MusicPost.objects.all().order_by('order')


        return context


