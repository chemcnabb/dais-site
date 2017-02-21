from django.contrib import admin
from watch.models import WatchPost
# Register your models here.
class WatchAdmin(admin.ModelAdmin):
    pass
admin.site.register(WatchPost, WatchAdmin)