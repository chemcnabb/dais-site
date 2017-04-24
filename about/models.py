from __future__ import unicode_literals
from tinymce.models import HTMLField
from django.db import models

# Create your models here.
class AboutPage(models.Model):
    header_text = HTMLField()