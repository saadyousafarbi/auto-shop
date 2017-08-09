from django.contrib import admin
from core.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'date_of_birth']

admin.site.register(Profile, ProfileAdmin)
