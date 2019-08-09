from django import forms
from .models import User,Topics

TITLE_CHOICES = {
    ('I','In Progress'),
    ('R', 'In Release'),
    ('P', 'Published'),

}


class UploadFileForm(forms.Form):

    author = forms.ModelChoiceField(queryset=User.objects.all())
    topic = forms.ModelChoiceField(queryset=Topics.objects.all())
    file = forms.FileField()
