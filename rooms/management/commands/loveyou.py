from django.core.management.base import BaseCommand

# 직접 커맨드 만들기!
class Command(BaseCommand):
    help = "This Command he is love me"
    print("hello")

    def add_arguments(self, parser):
        parser.add_argument(
            "--times",
            help="How many times do you want me to tell you that i love you?",
        )

    def handle(self, *args, **options):
        times = options.get("times")
        for t in range(0, int(times)):
            self.stdout.write(self.style.SUCCESS("i love you"))
