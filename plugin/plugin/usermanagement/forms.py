from django import forms

class AddUserForm(forms.Form):

    username = forms.CharField(max_length=25)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
