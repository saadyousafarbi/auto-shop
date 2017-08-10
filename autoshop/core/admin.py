from django.contrib import admin
from core.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'gender', 'date_of_birth']
    search_fields = ['user__username', 'user__gender']

admin.site.register(Profile, ProfileAdmin)
