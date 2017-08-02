from django import forms


class SignupForm(forms.Form):
    """
    Model signup form.

    fields:
        first_name (str): First name of user
        last_name (str): Last name of user
        email (str): Email of user
        password (str): Password of user

    """
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=100)
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class SigninForm(forms.Form):
    """
    Model signin form.

    fields:
        email (str): email of user
        password (str): password of user

    """
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

