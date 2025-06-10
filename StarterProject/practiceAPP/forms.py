from django import forms
from .models import image_store

class Image_from(forms.ModelForm):
    image_types = forms.ModelChoiceField(queryset=image_store.objects.all(), label="Image Type")