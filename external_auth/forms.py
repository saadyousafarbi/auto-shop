from django import forms


class PakwheelsLoginForm(forms.Form):
    """
    Pakwheels login form.
    """
    email = forms.CharField(help_text='Enter Pakwheels email', max_length=30)
    password = forms.CharField(help_text='Enter Pakwheels profile password', widget=forms.PasswordInput)
