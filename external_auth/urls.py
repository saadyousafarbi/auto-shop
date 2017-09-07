from django.conf.urls import url

from external_auth import views


app_name = 'external_auth'


urlpatterns = [
    url(r'^pakwheels/register/$', views.pakwheels_registration, name='pakwheels_registration'),
]
