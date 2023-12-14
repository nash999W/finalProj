
from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Image
        fields = ("title", "body", "image")
