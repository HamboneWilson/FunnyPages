from django.db import models

class ComicSeries(models.Model):

    name = models.CharField(max_length=200)
    homepage = models.URLField(max_length=200)
    def __unicode__(self):
        return self.name

class ComicImg(models.Model):

    series = models.ForeignKey(ComicSeries)
    name = models.CharField(max_length=200)
    img = models.FileField(upload_to='comic_img')
    def __unicode__(self):
        return self.name