from django.core.management.base import NoArgsCommand
from viewer.models import ComicSeries


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        #for each comic_series in the comic_series model
        for series in ComicSeries:
            series.download_newest_comic()
