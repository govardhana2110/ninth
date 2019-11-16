from django import forms
class NameForm(forms.Form):
    first_name = forms.CharField(label='firstname')
    second_name = forms.CharField(label='lastname')

