from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.template.defaultfilters import slugify

# Create your models here.
class PressPost(models.Model):
    date = models.DateTimeField()
    poster_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    subtitle = models.CharField(max_length=500,blank=True, null=True)
    credits = models.CharField(max_length=500,blank=True, null=True)
    url = models.CharField(max_length=500,blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    order = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def category(self):
        return "press"

    def get_url(self):
        return self.url

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(PressPost, self).save(*args, **kwargs)

