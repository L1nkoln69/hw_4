import random
import string

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    help = 'Create fake users'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('users', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        fake_user = Faker()
        number = options['users']

        def randompassword():
            chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
            size = random.randint(10, 12)
            return ''.join(random.choice(chars) for _ in range(size))
        for i in range(number):
            User.objects.create(username=fake_user.name(),
                                email=fake_user.email(), password=randompassword())
            self.stdout.write(self.style.SUCCESS('Successfully closed user "%s"' % i))
