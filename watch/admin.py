from django.contrib import admin
from watch.models import WatchPost
# Register your models here.
class WatchAdmin(admin.ModelAdmin):
    save_as=True
admin.site.register(WatchPost, WatchAdmin)