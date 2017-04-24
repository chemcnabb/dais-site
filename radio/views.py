from django.shortcuts import render
from django.views.generic import TemplateView
from radio.models import RadioPost, RadioSound
# Create your views here.
from django.shortcuts import get_object_or_404




class RadioView(TemplateView):
    template_name = "radio.html"

    def get_context_data(self, **kwargs):
        context = super(RadioView, self).get_context_data(**kwargs)
        # context["post_list"] = list(chain(WatchPost.objects.all(),LookPost.objects.all(), ListenPost.objects.all()))

        context["radio_posts"] = RadioPost.objects.all().order_by('order')


        return context


class SoundView(TemplateView):
    template_name = "sound.html"
    def get_context_data(self, **kwargs):
        slug = kwargs['sound_slug']
        context = super(SoundView, self).get_context_data(**kwargs)
        context["artist"] = get_object_or_404(RadioPost,slug=slug)

        return context