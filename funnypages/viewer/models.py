import os
from django.db import models
from django.core.urlresolvers import reverse
import requests
from bs4 import BeautifulSoup
from django.conf import settings
from datetime import datetime
from boto.s3.connection import S3Connection
from boto.s3.key import Key


class ComicSeries(models.Model):
    """A webcomic (eg. Penny Arcade, PvP, etc.)"""
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200)

    def __unicode__(self):
        return self.name

    def download_newest_comic(self):
        """Downloads the newest image for a webcomic and creates a ComicImg object for it"""
        newest_comic_url = self.get_newest_comic_url()
        comic_filename = newest_comic_url.split('/')[-1]
        #create a connection to the the image server
        conn = S3Connection(settings.ACCESS_KEY, settings.PASS_KEY)
        bucket = conn.get_bucket("funnypages")
        k = Key(bucket)
        image_path = 'comic_images/'
        bucket_check = os.path.join(image_path, comic_filename)

        #check the targeted file name against other comics in the comic_img media directory
        if bucket_check in bucket.list():
            return
        else:
            #use that object as an argument to download a target html resource to the comic image media subdirectory
            img_url = requests.get(newest_comic_url)
            img = open(comic_filename, 'wb')
            img.write(img_url.content)
            img.close()
            k.key = os.path.join(image_path, comic_filename)
            k.set_contents_from_filename(comic_filename)
            os.remove(comic_filename)
            #create an entry in the comic_img model and use the path of the downloaded image to create the img_field
            new_comic_image = ComicImg(name=comic_filename, series=self, pub_date=datetime.now())
            new_comic_image.save()
            
    def get_newest_comic_url(self):
        """Finds the url for a webcomic's newest image"""
        #create a beautiful soup instance for the target comic html
        soup = BeautifulSoup(requests.get(self.url).text)
        #use soup.find to return the src attribute of the target comic and store it in an object.
        if self.name == 'Dr. McNinja' or self.name == 'xkcd':
            return soup.find(id='comic').find('img').attrs['src']

        elif self.name == 'CTRL ALT DEL':
            return soup.find(id='content').find('img').attrs['src']

        else:
            raise Exception('%s is not a supported comic' % self.name)


class ComicImg(models.Model):
    """An comic page from a comic series"""
    series = models.ForeignKey(ComicSeries, related_name='images')
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        get_latest_by = "pub_date"

    def __unicode__(self):
        return self.name


class Collection(models.Model):
    """A collection of webcomics that can be called up for display"""
    name = models.CharField(max_length=200)
    user = models.ForeignKey("User")
    series = models.ManyToManyField(ComicSeries, related_name="collections")

    def __unicode__(self):
        return self.name

    @property
    def url(self):
        return reverse('viewer:viewer', kwargs={'collection_id': self.id})


class User(models.Model):
    """A class for storing user data"""
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 24)

    def __unicode__(self):
        return self.username


class SubmissionLog(models.Model):
    """A class for storing requests for new comics"""
    name = models.CharField(max_length=200)
    sub_date = models.DateTimeField()