from django.contrib import admin

# Register your models here.
from music.models import MusicPost
# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('artist_name','order')
    list_editable = ('order',)
admin.site.register(MusicPost, MusicAdmin)