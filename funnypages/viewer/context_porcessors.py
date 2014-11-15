from viewer.forms import CollectionSelectForm

def collection_drop_down(request):
    return {'collectionselectform':CollectionSelectForm()}
