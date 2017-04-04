from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import get_object_or_404
from press.models import PressPost


class PressView(TemplateView):
    template_name = "press.html"

    def get_context_data(self, **kwargs):
        context = super(PressView, self).get_context_data(**kwargs)
        # context["post_list"] = list(chain(WatchPost.objects.all(),LookPost.objects.all(), ListenPost.objects.all()))

        context["post_list"] = PressPost.objects.all().order_by('order')


        return context