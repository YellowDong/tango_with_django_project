from django import forms


class NameForm(forms.ModelForm):
    your_name = forms.CharField(max_length=100, label='your name')