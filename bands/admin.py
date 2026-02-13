from django.contrib import admin
from bands.models import Band


# Register your models here.
@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'formed_year', 'genre')
    search_fields = ('name', 'genre')
