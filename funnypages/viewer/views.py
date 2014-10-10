from django.shortcuts import render, get_object_or_404, redirect
from viewer.models import Collection, SubmissionLog
from viewer.forms import CollectionForm
from datetime import datetime
from django.views.generic import TemplateView


class LandingPageView(TemplateView):
    template_name = 'viewer/landingpage.html'


def edit(request, collection_id):
    collection = get_object_or_404(Collection, pk=collection_id)
    form = CollectionForm(instance=collection)
    if request.method == 'POST':
        if 'comicrequest' in request.POST:
            c = SubmissionLog(name=request.POST['newtitle'], sub_date=datetime.now())
            c.save()
        else:
            form = CollectionForm(request.POST, instance=collection)
            if form.is_valid():
                update_collection = form.save()
                return redirect('viewer:viewer', collection_id=update_collection.id)

    return render(request, 'viewer/edit.html', {'form': form})


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
    collection = get_object_or_404(Collection, pk=collection_id)
    return render(request, 'viewer/viewer.html', {'collection': collection})

