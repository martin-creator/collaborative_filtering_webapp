from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from recommender_system import utils as rs_utils


User = get_user_model() # get the currently active user model,


class Command(BaseCommand):
    '''Create fake users'''
    def add_arguments(self, parser: CommandParser) -> None:
        '''Add arguments to the command'''
        parser.add_argument('count', type=int, default=10, nargs='?')
        parser.add_argument('--movies', action='store_true', default=False)
        parser.add_argument('--users', action='store_true', default=False)
        parser.add_argument('--show-total', action='store_true', default=False)

    def handle(self, *args: Any, **options: Any) -> str | None:
       '''Handle the command'''
       count = options['count']
       show_total = options['show_total']
       load_movies = options['movies']
       generate_users = options['users']
       
       if load_movies:
           rs_utils.load_movie_data(limit=count)
           return self.stdout.write(self.style.SUCCESS(f'Loaded {count} movies'))
       
       if generate_users:
            profiles = rs_utils.get_fake_profiles(count=count)
            new_users = []
            for profile in profiles:
                new_users.append(User(**profile))
            user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Created {len(user_bulk)} users'))
            if show_total:
                    self.stdout.write(self.style.SUCCESS(f'Total users: {User.objects.count()}'))

        