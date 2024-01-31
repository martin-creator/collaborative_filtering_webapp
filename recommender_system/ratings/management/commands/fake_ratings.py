from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django.contrib.auth import get_user_model
from recommender_system import utils as rs_utils
from movies.models import Movie
from ratings.models import Rating
from ratings.tasks import generate_fake_reviews


User = get_user_model() # get the currently active user model,


class Command(BaseCommand):
    '''Create fake users'''
    def add_arguments(self, parser: CommandParser) -> None:
        '''Add arguments to the command'''
        parser.add_argument('count', type=int, default=10, nargs='?')
        parser.add_argument('--users', default=1000, type=int)
        parser.add_argument('--show-total', action='store_true', default=False)

    def handle(self, *args: Any, **options: Any) -> str | None:
       count = options['count']
       show_total = options['show_total']
       user_count = options['users']
       print(count, show_total, user_count)
       new_ratings = generate_fake_reviews(count=count, users=user_count)
       print(f"New ratings: {len(new_ratings)}")
       if show_total:
            qs = Rating.objects.all()
            print(f"Total ratings: {qs.count()}")