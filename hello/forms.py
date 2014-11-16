from django import forms
import datetime

class NameForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'YO Username', 'size' : '30px', 'required' : 'required' }), label='', max_length=128)
    message = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'YO Message', 'size' : '30px', 'required' : 'required' }), label='', max_length=400)
    time_left = forms.CharField(widget=forms.TextInput(attrs={'placeholder' : 'When do I YO?', 'size' : '30px', 'required' : 'required' }), label='', max_length=20)
