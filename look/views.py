from django.shortcuts import render
from django.views.generic import TemplateView
from look.models import LookPost
from django.shortcuts import get_object_or_404


class LookView(TemplateView):
    template_name = "look.html"
    def get_context_data(self, **kwargs):
        slug = kwargs['look_slug']
        context = super(LookView, self).get_context_data(**kwargs)

        context["look"] = get_object_or_404(LookPost, slug=slug)
        context["look_more"] = LookPost.objects.exclude(pk=context["look"].pk).order_by('order').order_by(
            '-date')[:3]

        return context