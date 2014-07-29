from django.forms import ModelForm
from viewer.models import Collection


class CollectionForm(ModelForm):
    class Meta:
        model = Collection