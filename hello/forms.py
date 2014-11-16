from django import forms
import datetime

class NameForm(forms.Form):
    username = forms.CharField(label='YO Username', max_length=128)
    message = forms.CharField(label='YO Message', max_length=400)
    time_left = forms.CharField(label='Time to YO', max_length=20)
