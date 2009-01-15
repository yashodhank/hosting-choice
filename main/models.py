import datetime
import base64
from django.db import models
from django.contrib.auth import models as auth

def slugify(data):
    """Turn a piece of data into a slug"""

    data = data.lower()
    data = re.sub('\s+', '-', data)
    return re.sub('[^a-z0-9\-]', '', data)


class Page(models.Model):
    """Store abitrary pages like About/Privacy/TOS in the database for easy updating"""
    name = models.CharField(max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    text = models.TextField()

    def __unicode__(self):
        return "/%s.html - %s" % (self.slug, self.name)

class Email(models.Model):
    """Emails gathered for the newsletter"""

    value = models.EmailField(max_length=255, unique=True)
    ip = models.CharField(max_length=25)
    active = models.BooleanField(default=True)


class Entry(models.Model):
    """Blog Entry"""

    title = models.CharField(max_length=255)
    user = models.ForeignKey(auth.User)
    slug = models.SlugField(max_length=255, unique=True)
    text = models.TextField()

    pub_date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return "%s - %s" % (self.title, self.user)
