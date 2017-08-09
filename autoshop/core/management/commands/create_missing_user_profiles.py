from django.contrib.auth.models import User
from django.core.management import BaseCommand

from core.models import Profile


class Command(BaseCommand):
    help = 'Create missing user profiles with empty values.'

    def handle(self, *args, **options):
        users_with_missing_profile = User.objects.filter(profile=None)
        self.create_user_profile(users_with_missing_profile)

        output_message = 'Created {missing_profiles_count} missing user profiles ' \
                         'out of total {total_users_count}.'.format(
                             missing_profiles_count=len(users_with_missing_profile),
                             total_users_count=User.objects.count()
                         )
        self.stdout.write(
            self.style.SUCCESS(output_message)
        )


    def create_user_profile(self, users_with_missing_profile):
        for user in users_with_missing_profile:
            Profile.objects.create(user=user)
