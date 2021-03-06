from django.contrib import admin
from look.models import LookPost, LookImage
# Register your models here.

class LookImageInline(admin.TabularInline):
    model = LookImage
    ordering = ("order",)
    extra=1

class LookAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('title',)

    inlines = [LookImageInline, ]
admin.site.register(LookPost, LookAdmin)
