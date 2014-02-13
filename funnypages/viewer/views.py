from annoying.decorators import render_to
from viewer.models import ComicSeries

@render_to('viewer/viewer.html')
def index(request):
    return {
        'comics': ComicSeries.objects.all()
    }
