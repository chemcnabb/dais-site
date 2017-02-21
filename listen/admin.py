from django.contrib import admin
from listen.models import ListenPost
# Register your models here.
class ListenAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('title',)
admin.site.register(ListenPost, ListenAdmin)
