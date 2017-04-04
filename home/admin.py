from django.contrib import admin

from home.models import HomePage
from listen.models import ListenPost
from look.models import LookPost
from merged_inlines.admin import MergedInlineAdmin
from watch.models import WatchPost


class WatchInline(admin.TabularInline):
    model = WatchPost
    exclude = ['subtitle','credits', 'detail','vimeo_id','description','slug', 'poster_image']

    max_num = 0

class LookInline(admin.TabularInline):
    model = LookPost
    exclude = ['subtitle', 'credits', 'detail', 'vimeo_id', 'description', 'slug', 'poster_image']

    max_num = 0


class ListenInline(admin.TabularInline):
    model = ListenPost
    exclude = ['subtitle', 'credits', 'detail', 'soundcloud_embed', 'description', 'slug', 'poster_image']

    max_num = 0

class HomeAdmin(MergedInlineAdmin):
    inlines = [WatchInline,LookInline, ListenInline]
    merged_field_order = ('title', 'date','order')
    merged_inline_order = 'order'

admin.site.register(HomePage,HomeAdmin)