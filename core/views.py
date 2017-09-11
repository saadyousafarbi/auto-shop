from __future__ import unicode_literals

from dateutil.parser import parse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from core.forms import SignupForm, SigninForm, EditProfileForm
from core.models import Profile


def index(request):
    """
    This view redirects users to the main page of autoshop website.
    """
    return render(request, 'home.html')


def register(request):
    """
    This view redirects users to the signup page. If user is submitting
    form (POST), user registration takes place. If user is visiting
    page, user is directed to page containing registration form.

    """
    if request.method == 'POST':
        post_data = request.POST.copy()
        post_data['date_of_birth'] = parse(post_data['date_of_birth'])
        form = SignupForm(post_data)
        if form.is_valid():
            new_user, created = User.objects.get_or_create(
                username=form.data['username']
            )
            if created:
                new_user.first_name = form.data['first_name']
                new_user.last_name = form.data['last_name']
                new_user.email = form.data['email']
                new_user.set_password(form.data['password'])
                new_user.profile.bio = form.data['bio']
                new_user.profile.gender = form.data['gender']
                new_user.profile.photo = form.data['photo']
                new_user.profile.date_of_birth = form.data['date_of_birth']
                new_user.profile.mobile_number = form.data['mobile_number']
                new_user.profile.address = form.data['address']
                new_user.profile.city = form.data['city']
                new_user.profile.country = form.data['country']
                new_user.is_active = True
                new_user.save()
                login(request, new_user)
                messages.success(
                    request,
                    'Registration was successful. Welcome to Auto-shop.',
                )
                return redirect('/')

        print 'Profile for user "%s" failed to save due to validation errors: %s' % (
            request.user.username, form.errors
        )
        messages.error(request, 'Form is invalid. Please try again.' + form.errors)
        return render(request, 'register.html')
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
                messages.error(request, 'Invalid credentials. Try again.')
                return render(request, 'login.html', {'form': form})

            login(request, user)
            messages.success(request, 'You logged in successfully.')
            return render(request, 'home.html')
    else:
        return render(request, 'login.html', {'form': form})


def log_out(request):
    """
    This view logs out the currently logged in user.
    """
    logout(request)
    return redirect('/')


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
    form = EditProfileForm(request.FILES, request.POST)
    user_profile = request.user.profile
    user_info_dict = {
        'user_id': request.user.id,
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
                photo=request.FILES['profile_photo'],
                mobile_number=form.data['mobile_number'],
                address=form.data['address'],
                city=form.data['city'],
                country=form.data['country'],
            )
            return redirect(reverse('core:profile'))

        print 'Profile for user "%s" failed to save due to validation errors: %s' % (
            request.user.username, form.errors
        )
        messages.error(request, 'Form is invalid', context)
        return render(request, 'profile_edit.html')

    return render(request, 'profile_edit.html', context)


def validate_username(request):
    """
    This view processes an AJAX request and tells whether a username is taken.
    """
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)
