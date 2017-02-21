from django.contrib import admin
from listen.models import ListenPost
# Register your models here.
class ListenAdmin(admin.ModelAdmin):
    pass
admin.site.register(ListenPost, ListenAdmin)
