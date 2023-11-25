from django import forms
from .models import SourceFormat, SourceURL

class SourceFormatForm(forms.ModelForm):
    class Meta:
        model = SourceFormat
        fields = ['name', 'description']

class SourceURLForm(forms.ModelForm):
    class Meta:
        model = SourceURL
        fields = ['name', 'description','url', 'format']
