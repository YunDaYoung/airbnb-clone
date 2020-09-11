from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This command creates facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="How many times do you want me to tell you that I love you", )

    def handle(self, *args, **options):
        facilities = [
            "엘레베이터",
            "건물 내 무료주차",
            "건물 외 무료주차",
            "헬스장",
            "수영장",
        ]

        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
