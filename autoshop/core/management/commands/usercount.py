from django.contrib.auth.models import User
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Number of users for auto-shop'

    def handle(self, *args, **options):
        user_count = User.objects.all().count()
        self.stdout.write(self.style.SUCCESS('Number of users: ' + str(user_count)))
