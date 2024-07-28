from django import forms

class InputForm(forms.Form):
    input_field = forms.CharField(label='Input', max_length=100)    