from django.shortcuts import render, get_object_or_404, redirect
from viewer.models import ComicSeries, Collection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from viewer.forms import CollectionForm


def homepage(request):
    return render(request, 'homepage')


def edit(request):
    return render(request, 'edit')


def create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            new_collection = form.save()
            return redirect('viewer', collection_id=new_collection.id)
    else:
        form = CollectionForm()

    return render(request, 'create', {
        'form': form,
    })


def viewer(request, collection_id):
    return render(request, 'viewer')

