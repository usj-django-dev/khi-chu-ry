from django import forms
from first_app import models

class Musician_Form(forms.ModelForm):
    class Meta:
        model = models.Musician
        fields = "__all__"

class Album_Form(forms.ModelForm):
    release_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields = "__all__"
