from django.shortcuts import render
from django.views.generic import TemplateView
from watch.models import WatchPost
from django.shortcuts import get_object_or_404
# Create your views here.


class WatchView(TemplateView):
    template_name = "watch.html"

    def get_context_data(self, **kwargs):
        slug = kwargs['watch_slug']
        context = super(WatchView, self).get_context_data(**kwargs)
        context["watch"] = get_object_or_404(WatchPost,slug=slug)
        context["watch_more"] = WatchPost.objects.all().order_by('-date').exclude(slug=slug)[:2]
        return context