from __future__ import unicode_literals

from dateutil.parser import parse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse

from core.forms import SignupForm, SigninForm, EditProfileForm
from core.models import Profile


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
            
        return render(request, 'failure.html')
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
                return render(request, 'failure.html')

            login(request, user)
            return render(request, 'success.html')
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
    user_profile = request.user.profile
    user_info_dict = {
        'username': user_profile.user,
        'bio': user_profile.bio,
        'gender': user_profile.gender,
        'date_of_birth': user_profile.date_of_birth,
        'mobile_number': user_profile.mobile_number,
        'address': user_profile.address,
        'city': user_profile.city,
        'country': user_profile.country,
    }
    context = {'user_info_dict': user_info_dict}
    return render(request, 'profile.html',  context)


@login_required()
def edit_profile(request):
    """
    Show profile edit page and save user profile information on save.
    """
    form = EditProfileForm()
    user_profile = request.user.profile
    user_info_dict = {
        'username': request.user,
        'bio': user_profile.bio,
        'gender': user_profile.gender,
        'date_of_birth': user_profile.date_of_birth,
        'mobile_number': user_profile.mobile_number,
        'address': user_profile.address,
        'city': user_profile.city,
        'country': user_profile.country,
        'photo': user_profile.photo,
    }
    context = {'user_info_dict': user_info_dict, 'form': form}
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['date_of_birth'] = parse(post_data['date_of_birth'])
        form = EditProfileForm(post_data, instance=user_profile)
        if form.is_valid():
            Profile.objects.filter(user=request.user).update(
                bio=form.data['bio'],
                gender=form.data['gender'],
                mobile_number=form.data['mobile_number'],
                address =form.data['address'],
                city=form.data['city'],
                country=form.data['country'],
            )
            return redirect(reverse('core:profile'))

        print 'Profile for user "%s" failed to save due to validation errors: %s' % (
            request.user.username, form.errors
        )
        return render(request, 'failure.html')

    return render(request, 'profile_edit.html', context)
