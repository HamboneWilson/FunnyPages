from django.db import models

class ComicSeries(models.Model):
    """A webcomic (eg. Penny Arcade, PvP, etc.)"""
    name = models.CharField(max_length=200)
    homepage = models.URLField(max_length=200)
    collections = models.ManyToManyField("Collection")

    def __unicode__(self):
        return self.name

class ComicImg(models.Model):
    """An comic page from a comic series"""
    series = models.ForeignKey(ComicSeries, related_name='images')
    name = models.CharField(max_length=200)
    img = models.FileField(upload_to='comic_img/')
    pub_date = models.DateTimeField()

    class Meta:
        get_latest_by = "pub_date"

    def __unicode__(self):
        return self.name

class Collection(models.Model):
    """A collection of webcomics that can be called up for display"""
    name = models.CharField(max_length=200)
    user = models.ForeignKey("User")

    def __unicode__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 24)

    def __unicode__(self):
        return self.username