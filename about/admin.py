from django.contrib import admin
from about.models import AboutPage
# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    pass

admin.site.register(AboutPage, AboutAdmin)