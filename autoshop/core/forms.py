from core.models import Profile
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


class SignupForm(ModelForm):
    """
    Model signup form.

    fields:
        first_name (str): First name of user
        last_name (str): Last name of user
        email (str): Email of user
        password (str): Password of user

    """
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    bio = forms.CharField(help_text='Enter some information about yourself', required=False)
    gender = forms.ChoiceField(help_text='Specify gender', choices=GENDER_CHOICES)
    photo = forms.ImageField(help_text='Upload profile photo', required=False)
    date_of_birth = forms.DateField(help_text='Enter date of birth', required=False)
    mobile_number = forms.CharField(help_text='Enter mobile number', required=False)
    address = forms.CharField(help_text='Enter address', required=False)
    city = forms.CharField(help_text='Enter city', required=False)
    country = forms.CharField(help_text='Enter country', required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        help_texts = {
            'first_name': 'Enter first name:',
            'last_name': 'Enter last name:',
            'username': 'Enter username:',
            'email': 'Enter email:',
            'password': 'Enter password:',
        }


class SigninForm(forms.Form):
    """
    Model signin form.

    fields:
        email (str): email of user
        password (str): password of user

    """
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class EditProfileForm(ModelForm):
    """
    Edit Profile form.
    """
    class Meta:
        model = Profile
        exclude = ['user', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class':'datepicker'}),
        }
