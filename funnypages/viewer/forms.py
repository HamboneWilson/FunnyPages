from django.forms import ModelForm, CheckboxSelectMultiple, ModelChoiceField, TextInput, HiddenInput
from viewer.models import Collection, SubmissionLog


class CollectionForm(ModelForm):
    """A for for creating new collections on the create page"""
    class Meta:
        model = Collection
        fields = ('name', 'user', 'series')
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Collection Name'}),
            'series': CheckboxSelectMultiple(),
            'user': HiddenInput(),
        }


# class SelectForm(ModelForm):
#     """A form for selecting a collection to view in the header of every page"""
#     form = ModelChoiceField(queryset=Collection.objects.all(), empty_label='View a Collection')
#
#
# class SubmissionForm(ModelForm):
#     """A form for submitting time stamped requests for new comics"""
#     class Meta:
#         model = SubmissionLog
#         fields = ('name', 'sub_date')
#         widgets = {
#             'name': TextInput(attrs={'placeholder': 'Series Name'}),
#             'sub_date': HiddenInput(),
#         }