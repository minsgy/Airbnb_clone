import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models


# 실험 할 유저 생성하는 COMMAND
class Command(BaseCommand):
    help = "This Command creates many list"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help="How many list do you want to create?",
        )

    def handle(self, *args, **options):  # 커맨드 실행 시 실행

        number = options.get("number")
        seeder = Seed.seeder()

        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        seeder.add_entity(
            list_models.List,
            number,
            {
                "user": lambda x: random.choice(users),
            },
        )
        created = seeder.execute()
        cleaned = flatten(list(created.values()))

        for pk in cleaned:
            list_obj = list_models.List.objects.get(pk=pk)
            to_add = rooms[random.randint(1, 3) : random.randint(6, 10)]
            # to_add = rooms[0~5:6~30] slicing
            list_obj.rooms.add(*to_add)  # array 값이 되기 때문에, 요소만 가져옴.

        self.stdout.write(self.style.SUCCESS(f"{number} List created!"))  # 오브젝트 생성

