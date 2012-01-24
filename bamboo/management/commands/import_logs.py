from django.core.management.base import BaseCommand

class Commmand(BaseCommand):
    args = ""
    help = ""

    def handle(self, *args, **options):
        print "Testing"
