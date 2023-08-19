from django.core.management import BaseCommand

from api.models import BookmarkType


def populate_bookmark_types():
    for name in ('website', 'book', 'article', 'music', 'video'):
        BookmarkType.objects.get_or_create(name=name)


class Command(BaseCommand):
    help = 'Заполнить базу данных начальными данными'

    def add_arguments(self, parser):
        parser.add_argument('-n', '--noinput', action='store_true', help='Не запрашивать подтверждение')

    def handle(self, *args, **options):
        no_input = options.get('noinput')
        if no_input:
            self.stdout.write('Заполнение началось')
            populate_bookmark_types()
            self.stdout.write('Заполнение завершено')
        else:
            answer = input('Вы уверены, что хотите удалить все данные и заполнить их заново? (y/n) ')
            if answer == 'y':
                self.stdout.write('Заполнение началось')
                populate_bookmark_types()
                self.stdout.write('Заполнение завершено')
            else:
                self.stdout.write('Заполнение отменено')
