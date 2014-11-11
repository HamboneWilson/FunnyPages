from django.core.management.base import NoArgsCommand
from viewer.models import ComicSeries


class Command(NoArgsCommand):

    def handle_noargs(self, **options):
        """Get the newest comic for every series on Funnypages"""
        s = ComicSeries.objects.all()
        for series in s:
            series.download_newest_comic()
