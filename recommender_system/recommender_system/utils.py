from faker import Faker
import csv
from pprint import pprint
from  django.conf import settings

MOVIE_METADATA_CSV = settings.DATA_DIR / "movies_metadata.csv"

def load_movie_data(limit=10):
    '''Load movie data from csv file'''
    with open(MOVIE_METADATA_CSV, encoding='utf-8', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            if i == limit:
                break
            pprint(row)
            print('-------------------')


def get_fake_profiles(count=10):
    '''Generate fake profiles'''
    fake = Faker()
    user_data = []

    for _ in range(count):
        profile = fake.profile()
        data = {
            'username': profile['username'],
            'email': profile['mail'],
            'is_active': True,
        }

        if 'name' in profile:
            fname, lname = profile['name'].split(' ')[:2]
            data['first_name'] = fname
            data['last_name'] = lname
        
        user_data.append(data)
    return user_data