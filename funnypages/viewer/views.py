from django.shortcuts import render, get_object_or_404, redirect
from viewer.models import ComicSeries, Collection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from viewer.forms import CollectionForm


def homepage(request):
    return render(request, 'viewer/homepage.html')


def newcomic(request):
    return render(request, 'viewer/newcomic.html')


def create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect()
    return render(request, 'viewer/create.html')


def viewer(request):
    return render(request, 'viewer/viewer.html')

