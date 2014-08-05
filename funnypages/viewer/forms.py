from django.forms import ModelForm, CheckboxSelectMultiple, MultipleChoiceField, TextInput, HiddenInput
from viewer.models import Collection, ComicSeries


class CollectionForm(ModelForm):

    class Meta:
        model = Collection
        fields = ('name', 'user', 'series')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Collection Name'}),
            'series': CheckboxSelectMultiple(),
            'user': HiddenInput(),
        }