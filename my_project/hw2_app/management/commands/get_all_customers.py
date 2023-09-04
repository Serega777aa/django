from django.core.management import BaseCommand

from hw2_app.models import Customer


class Command(BaseCommand):
    help = "Get all customers."

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()

        self.stdout.write(f'{customers}')
