from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from dais.utilities import unique_slugify as slugify

# Create your models here.
class LookPost(models.Model):
    date = models.DateTimeField()
    poster_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    subtitle = models.CharField(max_length=500,blank=True, null=True)
    credits = models.CharField(max_length=500,blank=True, null=True)
    detail = models.CharField(max_length=500,blank=True, null=True)
    vimeo_id = models.CharField(max_length=500, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def category(self):
        return "look"

    def get_url(self):
        return "/look/%s" % self.slug

    def save(self, *args, **kwargs):
        self.slug = slugify(self, self.title)
        super(LookPost, self).save(*args, **kwargs)