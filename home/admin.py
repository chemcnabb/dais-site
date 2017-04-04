from django.contrib import admin
from merged_inlines.admin import MergedInlineAdmin
from home.models import HomePage
from watch.models import WatchPost
from listen.models import ListenPost
from look.models import LookPost

class WatchInline(admin.TabularInline):
    model = WatchPost
    exclude = ['date','subtitle','credits', 'detail','vimeo_id','description','slug', 'poster_image']
    ordering = ("order","date",)
    max_num = 0

class LookInline(admin.TabularInline):
    model = LookPost
    exclude = ['date', 'subtitle', 'credits', 'detail', 'vimeo_id', 'description', 'slug', 'poster_image']
    ordering = ("order", "date",)
    max_num = 0


class ListenInline(admin.TabularInline):
    model = ListenPost
    exclude = ['date', 'subtitle', 'credits', 'detail', 'soundcloud_embed', 'description', 'slug', 'poster_image']
    ordering = ("order", "date",)
    max_num = 0

class HomeAdmin(MergedInlineAdmin):
    inlines = [WatchInline,LookInline, ListenInline]

admin.site.register(HomePage,HomeAdmin)