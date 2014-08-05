from django.shortcuts import render, get_object_or_404, redirect
from viewer.models import ComicSeries, Collection
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from viewer.forms import CollectionForm


def landingpage(request):
    return render(request, 'viewer/landingpage.html')


def edit(request):
    return render(request, 'viewer/edit.html')


def create(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            new_collection = form.save()
            return redirect('viewer:viewer', collection_id=new_collection.id)
    else:
        form = CollectionForm(initial={'user': '1'})

    return render(request, 'viewer/create.html', {
        'form': form,
    })


def viewer(request, collection_id):
    return render(request, 'viewer/viewer.html')

