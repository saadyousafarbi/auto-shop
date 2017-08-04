from django.conf.urls import url

from . import views

app_name = 'core'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^failure', views.failure, name='failure'),
    url(r'^success', views.success, name='success'),
    url(r'^login', views.log_in, name='login'),
    url(r'^logout', views.log_out, name='log_out'),
    url(r'^profile', views.profile, name='profile'),
]
