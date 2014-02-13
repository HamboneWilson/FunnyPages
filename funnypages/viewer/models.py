from django.db import models

class ComicSeries(models.Model):
    """A webcomic (eg. Penny Arcade, PvP, etc.)"""
    name = models.CharField(max_length=200)
    homepage = models.URLField(max_length=200)

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