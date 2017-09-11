from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from external_auth.forms import PakwheelsLoginForm
from external_auth.pakwheels_profile import PakwheelsProfile
from external_auth.pakwheels_scraper import PakwheelsScraper
from django.shortcuts import render
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def pakwheels_registration(request):
    if request.method == 'GET':
        pakwheels_login_form = PakwheelsLoginForm()
        context = {'form': pakwheels_login_form}
        return render(request, 'pakwheels_register.html', context)

    pakwheels_login_form = PakwheelsLoginForm(request.POST)
    email = pakwheels_login_form.data['email']
    password = pakwheels_login_form.data['password']
    pakwheels_scraper = PakwheelsScraper(
        email,
        password,
    )
    pakwheels_profile_response = pakwheels_scraper.login_and_retrieve_profile()
    if pakwheels_profile_response:
        pakwheels_profile = PakwheelsProfile(
            first_name=pakwheels_profile_response['first_name'],
            last_name=pakwheels_profile_response['last_name'],
            gender=pakwheels_profile_response['user_gender'],
            user_name=pakwheels_profile_response['user_name'],
            password=password,
            email=pakwheels_profile_response['user_email'],
            birthday=pakwheels_profile_response['user_birthday'],
            city=pakwheels_profile_response['user_city'],
            country=pakwheels_profile_response['user_country'],
        )
        user, is_created = User.objects.get_or_create(
            username=pakwheels_profile.user_name
        )
        if is_created:
            user.first_name = pakwheels_profile.first_name
            user.last_name = pakwheels_profile.last_name
            user.email = pakwheels_profile.email
            user.set_password(pakwheels_profile.password)
            user.profile.gender = pakwheels_profile.gender
            user.profile.date_of_birth = pakwheels_profile.birthday
            user.profile.city = pakwheels_profile.city
            user.profile.country = pakwheels_profile.country
            user.is_active = True
            user.save()
            login(request, user)
            messages.success(
                request,
                'Pakwheels login successful.'
                ' We have registered you on our website with same credentials.'
                ' You can change your password.',
            )
            return render(request, 'home.html')

    else:
        messages.error(request, 'The Pakwheels credentials are incorrect. Please try again.')
        return render(request, 'pakwheels_register.html', context={'form': pakwheels_login_form})

