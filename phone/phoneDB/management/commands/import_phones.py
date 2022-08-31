from django.core.management.base import BaseCommand
import csv

from django.utils.text import slugify

from phoneDB.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('D:\\Мои документы\\PhoneDB.Django\\phones.csv', "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=";"))
            for row in data[1:]:
                Phone.objects.create(
                    id=row[0],
                    name=row[1],
                    image=row[2],
                    price=row[3],
                    release_date=row[4],
                    lte_exists=row[5],
                    slug=slugify(row[1])

                )
