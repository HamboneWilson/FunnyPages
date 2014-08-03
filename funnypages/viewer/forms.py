from django.forms import ModelForm, CheckboxSelectMultiple
from viewer.models import Collection


class CollectionForm(ModelForm):

    class Meta:
        model = Collection
        fields = ('name', 'user', 'series')
        widgets = {
            'series': CheckboxSelectMultiple,
        }