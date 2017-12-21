from django import forms
from youtubeadl.models import Files

class FileForm(forms.ModelForm):
  class Meta:
    model = Files
    fields = {'description','file'}
    