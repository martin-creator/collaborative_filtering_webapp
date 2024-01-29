from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ratings.models import Rating
from django.utils import timezone
import datetime

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating) # this is the generic relation queryset 
    rating_last_updated = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    rating_count = models.IntegerField(blank=True, null=True)
    rating_avg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def rating_avg_display(self):
        now = timezone.now()

        if not self.rating_last_updated:
            return self.calculate_ratings()
        
        if now > datetime.timedelta(minutes=1):
            return self.rating_avg

        return self.calculate_ratings()
    
    def calculate_ratings_count(self):
        return self.ratings.all().count()
    
    def calculate_ratings_avg(self):
        return self.ratings.all().avg()
    
    def calculate_ratings(self,save=True):
        rating_avg = self.calculate_ratings_avg()
        rating_count = self.calculate_ratings_count()
        self.rating_avg = rating_avg
        self.rating_count = rating_count
        self.rating_last_updated = timezone.now()
        if save:
            self.save()
        return rating_avg