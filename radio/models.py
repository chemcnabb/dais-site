from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.template.defaultfilters import slugify
from home.models import HomePage

class RadioPage(models.Model):
    header_text = HTMLField()

class RadioPost(models.Model):
    date = models.DateTimeField()
    poster_image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=500,blank=True, null=True)
    subtitle = models.CharField(max_length=500,blank=True, null=True)
    credits = models.CharField(max_length=500,blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    order = models.IntegerField(default=0)
    # home = models.ForeignKey(HomePage, default=1)

    def __unicode__(self):
        return self.title

    def category(self):
        return "look"

    def get_url(self):
        return "/radio/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(RadioPost, self).save(*args, **kwargs)

class RadioSound(models.Model):
    image = models.ImageField(blank=True, null=True)
    soundcloud_embed = models.CharField(max_length=500, blank=True, null=True)
    credits = models.CharField(max_length=500, blank=True, null=True)
    description = HTMLField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True, default=0)
    post = models.ForeignKey("RadioPost", null=True, blank=True)
    def __unicode__(self):
        if self.image:
            return self.image.url.split("/")[-1].split(".")[0]
        else:
            return "image"

    class Meta:
        ordering = ['order']