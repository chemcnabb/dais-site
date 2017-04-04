from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.template.defaultfilters import slugify

# Create your models here.
class MusicPost(models.Model):
    date = models.DateTimeField()
    poster_image = models.ImageField(blank=True, null=True)
    artist_name = models.CharField(max_length=500,blank=True, null=True)
    bio = HTMLField(blank=True, null=True)
    soundcloud_embed = models.CharField(max_length=500, blank=True, null=True)
    order = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, null=True)

    def __unicode__(self):
        return self.artist_name

    def category(self):
        return "music"

    def get_url(self):
        return "/artist/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.artist_name)
        super(MusicPost, self).save(*args, **kwargs)

