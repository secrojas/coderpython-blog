from django import forms

class SearchPost(forms.Form):
    title = forms.CharField(max_length=50)