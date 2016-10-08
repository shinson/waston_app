from django import forms
from django.http import HttpResponse
from django.conf import settings

#Watson Dependencies
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1

#Get APIKEY variable from settings
APIKEY = getattr(settings, "APIKEY", None)

# Watson authentication
alchemy_language = AlchemyLanguageV1(api_key=APIKEY)

class CommentForm(forms.Form):
    comment = forms.CharField(label="Comment", widget=forms.Textarea(attrs={'rows': 10}), required =True)

    def ask_watson(self):
        text = self.cleaned_data['comment']
        combined_operations = ['doc-sentiment']
        return alchemy_language.combined(text=text, extract=combined_operations)
