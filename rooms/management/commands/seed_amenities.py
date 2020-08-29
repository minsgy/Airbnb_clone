from django.core.management.base import BaseCommand
from rooms.models import Amenity

# 편의 시설 생성 COMMAND
class Command(BaseCommand):
    help = "This Command creates amenities"

    # def add_arguments(self, parser):
    # parser.add_argument(
    #         "--times",
    #         help="How many times do you want me to tell you that i love you?",
    #     )
    def handle(self, *args, **options):  # 커맨드 실행 시 실행 값
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air-conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High-chair",
            "Self-checkin",
            "Smoke-alarm",
            "monoxide-alarm",
            "Private-bathroom",
            "Piano",
            "Beachfront",
            "Waterfront",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)  # 모듈.오브젝트.명령어()
        self.stdout.write(self.style.SUCCESS("Amenities created!"))  # 오브젝트 생성 성공

    # def handle(self, *args, **options):
    #     times = options.get("times")
    #     for t in range(0, int(times)):
    #         self.stdout.write(self.style.SUCCESS("i love you"))
