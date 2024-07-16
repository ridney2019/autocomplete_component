import json
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from search_app.models import Item

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'data.json')
        with open(file_path, 'r') as f:
            data = json.load(f)
            for item in data:
                Item.objects.create(name=item['name'])
        self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
