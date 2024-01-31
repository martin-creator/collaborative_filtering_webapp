from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'calculate_ratings_count'
    , 'rating_last_updated']
    readonly_fields = ['rating_avg', 'rating_avg_display' 'calculate_ratings_count']

admin.site.register(Movie, MovieAdmin)