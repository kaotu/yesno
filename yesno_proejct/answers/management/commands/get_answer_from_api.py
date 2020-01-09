from django.core.management.base import BaseCommand

import requests

from answers.models import Answer


class Command(BaseCommand):
    help = 'Get Answer from API of http://yesno.wtf/api/'

    def add_arguments(self, parser):
        parser.add_argument('forced_type', 
        type=str,
        help='you can force by send "yes" or "no"')

    def handle(self, *args, **options):
        params = options['forced_type']
        url = f'http://yesno.wtf/api/?force={params}'
        response = requests.get(url)
        data = response.json()
        answer = Answer.objects.create(text=data['answer'], image=data['image'])
        display = f'created: {str(answer.id)} {answer.text} {answer.image}'
        self.stdout.write(display)