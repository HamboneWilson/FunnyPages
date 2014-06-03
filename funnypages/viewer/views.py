from annoying.decorators import render_to
from viewer.models import ComicSeries
from django.http import HttpResponse

@render_to('viewer/viewer.html')
def index(request):
    return {
        'comics': ComicSeries.objects.all()
    }
def homepage(request):
    return HttpResponse("You are at the funnypages home page")
def request(request):
    return HttpResponse("You are at the funnypages request a comic page")
def create(request):
    return HttpResponse("You are at the funnypages create a collection page")
