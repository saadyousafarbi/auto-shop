from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import SignupForm, SigninForm


def index(request):
    """
    This view redirects users to the main page of autoshop website.
    """
    return render(request, 'base.html')


def register(request):
    """
    This view redirects users to the signup page. If user is submitting
    form (POST), user registration takes place. If user is visiting
    page, user is directed to page containing reqistration form.

    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user, created = User.objects.get_or_create(
                username=form.data['username']
            )
            if created:
                new_user.first_name = form.data['first_name']
                new_user.last_name = form.data['last_name']
                new_user.email = form.data['email']
                new_user.set_password(form.data['password'])
                new_user.save()
                return redirect('/')
        return redirect('failure.html')
    else:
        form = SignupForm()
        return render(request, 'register.html', {'form': form})


def log_in(request):
    """
    This view handles the sign in process of the website. It checks whether
    a user is submitting (POST) his credentials or whether a user is
    requesting a user sign in form to submit his/her credentials.

    """
    form = SigninForm()
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.data['username'],
                password=form.data['password'],
            )
            if not user:
                return redirect('failure.html')

            login(request, user)
            return redirect('success.html')
    else:
        return render(request, 'login.html', {'form': form})


def log_out(request):
    """
    This view logs out the currently logged in user.
    """
    logout(request)
    return redirect('/')


@login_required()
def success(request):
    """
    This view directs user to success page in case of successful logistration.

    """
    return render(request, 'success.html')


def failure(request):
    """
    This view directs user to failure page in case of wrong logistration.
    """
    return render(request, 'failure.html')


@login_required()
def profile(request):
    """
    This view directs current user to his/her profile page
    """
    username = request.user
    user_information = User.objects.get(username=username)
    user_info_dict = {
        'username' : user_information.username,
        'first_name': user_information.first_name,
        'last_name': user_information.last_name,
        'email' : user_information.email,
    }
    context = {'user_info_dict': user_info_dict}
    return render(request, 'profile.html',  context)
