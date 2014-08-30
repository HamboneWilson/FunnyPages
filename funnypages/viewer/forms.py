from django import forms
from viewer.models import Collection, SubmissionLog


class CollectionForm(forms.ModelForm):
    """A for for creating new collections on the create page"""
    class Meta:
        model = Collection
        fields = ('name', 'user', 'series')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Collection Name'}),
            'series': forms.CheckboxSelectMultiple(),
            'user': forms.HiddenInput(),
        }


class CollectionSelectForm(forms.Form):
    """A form for selecting a collection to view in the header of every page"""
    collections = forms.ModelChoiceField(queryset=Collection.objects.all(), empty_label='View a Collection')
#
#
# class SubmissionForm(forms.ModelForm):
#     """A form for submitting time stamped requests for new comics"""
#     class Meta:
#         model = SubmissionLog
#         fields = ('name', 'sub_date')
#         widgets = {
#             'name': forms.TextInput(attrs={'placeholder': 'Series Name'}),
#             'sub_date': forms.HiddenInput(),
#         }