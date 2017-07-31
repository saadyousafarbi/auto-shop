from django.conf.urls import url

from . import views

app_name = 'welcome'
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
]
