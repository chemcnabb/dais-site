from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.shortcuts import get_object_or_404
from listen.models import ListenPost

class ListenView(TemplateView):
    template_name = "listen.html"
    def get_context_data(self, **kwargs):
        slug = kwargs['listen_slug']
        context = super(ListenView, self).get_context_data(**kwargs)
        context["listen"] = get_object_or_404(ListenPost,slug=slug)
        context["listen_more"] = ListenPost.objects.exclude(pk=context["listen"].pk).order_by('order').order_by('-date')[:3]
        return context