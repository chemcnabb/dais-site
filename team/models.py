from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
# Create your models here.
from django.template.defaultfilters import slugify

# Create your models here.
class TeamMember(models.Model):
    date = models.DateTimeField()
    poster_image = models.ImageField(blank=True, null=True)
    full_name = models.CharField(max_length=500,blank=True, null=True)
    role = models.CharField(max_length=500,blank=True, null=True)
    description = HTMLField(blank=True, null=True)

    slug = models.SlugField(blank=True, null=True)

    def __unicode__(self):
        return self.full_name

    def category(self):
        return "team"

    def get_url(self):
        return "/team/%s" % self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(TeamMember, self).save(*args, **kwargs)

