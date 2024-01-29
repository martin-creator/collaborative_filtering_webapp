from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255, unique=True)
    overview = models.TextField()
    release_date = models.DateField(blank=True, null=True, auto_now=False, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    # rating = GenericRelation(Rating, related_query_name='movies')

