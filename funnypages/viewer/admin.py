from django.contrib import admin

from viewer.models import ComicImg, ComicSeries, Collection, User

admin.site.register(ComicImg)
admin.site.register(ComicSeries)
admin.site.register(User)
admin.site.register(Collection)
