from django import forms

class NameForm(forms.Form):
    You = forms.CharField(label='You', max_length=100)