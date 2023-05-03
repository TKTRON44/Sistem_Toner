from django import forms
from .models import Toner

class SelectTonerForm(forms.Form):
    toner = forms.ModelChoiceField(queryset=Toner.objects.all(), empty_label=None, widget=forms.RadioSelect)
