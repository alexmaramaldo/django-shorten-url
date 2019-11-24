from django import forms
from core.models import Link

class LinkForm(forms.Form):
    url = forms.URLField(label='Your link', max_length=100)
    class Meta:
        model = Link
        fields = ['url']