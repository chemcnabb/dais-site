from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models
from django.template.defaultfilters import slugify
from home.models import HomePage

# Create your models here.
class WatchPost(models.Model):
    date = models.DateTimeField()
    poster_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    subtitle = models.CharField(max_length=500,blank=True, null=True)
    credits = models.CharField(max_length=500,blank=True, null=True)
    detail = models.CharField(max_length=500,blank=True, null=True)
    vimeo_id = models.CharField(max_length=500, blank=True, null=True)
    youtube_embed = models.CharField(max_length=500, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    order = models.IntegerField(default=0)
    home = models.ForeignKey(HomePage, default=1)
    def __unicode__(self):
        return self.title

    def category(self):
        return "watch"

    def get_url(self):
        return "/watch/%s" % self.slug



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(WatchPost, self).save(*args, **kwargs)