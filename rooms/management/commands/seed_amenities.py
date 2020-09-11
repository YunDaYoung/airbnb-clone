from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help="How many times do you want me to tell you that I love you", )

    def handle(self, *args, **options):
        amenities = [
            "주방",
            "난방",
            "세탁기",
            "Wi-Fi",
            "실내 벽난로",
            "노트북 작업 공간",
            "침대",
            "셀프 체크인",
            "일산화탄소 감지기",
            "샴푸",
            "에어컨",
            "드라이어",
            "아침 식사",
            "행거",
            "헤어 드라이어",
            "TV",
            "유아용 의자",
            "연기 감지기",
            "개인 화장실",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created"))