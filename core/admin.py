from django.contrib import admin
from core.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'date_of_birth']
    search_fields = ['user__username']

admin.site.register(Profile, ProfileAdmin)
