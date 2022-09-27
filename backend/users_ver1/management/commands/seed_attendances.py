from django.core.management.base import BaseCommand
from django_seed import Seed
from attendance.models import Attendance
from users.models import User
import random

class Command(BaseCommand):

    help = "This Command Creates Attendances"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many attendances do you want to create"
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        seeder = Seed.seeder()

        users = User.objects.all()

        seeder.add_entity(
            Attendance,
            number,
            {
                "user": lambda x: random.choice(users),
            }
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} attendances created!"))
