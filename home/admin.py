from django.contrib import admin
from merged_inlines.admin import MergedInlineAdmin
from home.models import HomePage
from watch.models import WatchPost
from listen.models import ListenPost
from look.models import LookPost

class WatchInline(admin.TabularInline):
    model = WatchPost

class LookInline(admin.TabularInline):
    model = LookPost

class ListenInline(admin.TabularInline):
    model = ListenPost

class HomeAdmin(MergedInlineAdmin):
    inlines = [WatchInline,LookInline, ListenInline]

admin.site.register(HomePage,HomeAdmin)