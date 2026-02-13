from django.contrib import admin
from concerts.models import Concert, SetlistEntry


# Register your models here.
class SetlistEntryInline(admin.TabularInline):
    model = SetlistEntry
    extra = 1

@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('band', 'venue', 'city', 'date')
    list_filter = ('band', 'city', 'date')
    inlines = [SetlistEntryInline]

@admin.register(SetlistEntry)
class SetlistEntryAdmin(admin.ModelAdmin):
    list_display = ('concert', 'song', 'order', 'encore')
    list_filter = ('encore',)
