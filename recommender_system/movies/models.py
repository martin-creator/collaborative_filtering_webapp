from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ratings.models import Rating

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    ratings = GenericRelation(Rating) # this is the generic relation queryset 


    def calculate_ratings_count(self):
        return self.ratings.all().count()
    
    def calculate_ratings_avg(self):
        return self.ratings.avg()
