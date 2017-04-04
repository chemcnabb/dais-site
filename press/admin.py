from django.contrib import admin

# Register your models here.
from press.models import PressPost
# Register your models here.
class PressAdmin(admin.ModelAdmin):
    save_as = True
    list_display = ('title','order')
    list_editable = ('order',)
admin.site.register(PressPost, PressAdmin)