from django.contrib import admin
from .models import Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ['user', 'value', 'content_type', 'active']
    raw_id_fields = ['user']
    readonly_fields = ['content_type']


admin.site.register(Rating, RatingAdmin)
