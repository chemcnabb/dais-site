from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.template.defaultfilters import slugify

# Create your models here.
class ListenPost(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    poster_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    subtitle = models.CharField(max_length=500,blank=True, null=True)
    credits = models.CharField(max_length=500,blank=True, null=True)
    detail = models.CharField(max_length=500,blank=True, null=True)
    soundcloud_embed = models.CharField(max_length=500, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def category(self):
        return "listen"

    def get_url(self):
        return "/listen/%s" % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(ListenPost, self).save(*args, **kwargs)