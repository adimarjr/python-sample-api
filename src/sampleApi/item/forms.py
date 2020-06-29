from django import forms
from .models import Item

class ItemForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)

class ItemModelForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']