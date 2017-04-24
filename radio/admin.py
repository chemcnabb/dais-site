from django.contrib import admin
from radio.models import RadioPost, RadioSound, RadioPage
# Register your models here.

class RadioPageAdmin(admin.ModelAdmin):
    pass

admin.site.register(RadioPage, RadioPageAdmin)

class SoundInline(admin.TabularInline):
    model = RadioSound
    ordering = ("order",)
    extra=1

class RadioPostAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('title',)

    inlines = [SoundInline, ]
admin.site.register(RadioPost, RadioPostAdmin)