"""dais URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from home.views import HomeView
from watch.views import WatchView
from look.views import LookView
from listen.views import ListenView
from django.conf.urls.static import static
from radio.views import RadioView
from music.views import MusicView
from about.views import AboutView
from team.views import TeamView
from django.views.generic import TemplateView
from django.conf.urls import include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),
    url(r"^watch/(?P<watch_slug>\w+)/$", WatchView.as_view(), name="watch"),
    url(r'^look/(?P<look_slug>\w+)/$', LookView.as_view(), name="look"),
    url(r'^listen/(?P<listen_slug>\w+)/$', ListenView.as_view(), name="listen"),
    url(r'^radio/$', RadioView.as_view(), name="radio"),
    url(r'^music/$', MusicView.as_view(), name="music"),
    url(r'^events/', include('happenings.urls', namespace='calendar'), name="events"),
# url(r'^calendar/', include('happenings.urls', namespace='calendar')),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^team/$', TeamView.as_view(), name="team"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
