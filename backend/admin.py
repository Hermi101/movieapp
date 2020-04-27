from django.contrib import admin

# Register your models here.
from .models import Movie, Genre, Person, PersonMovie, CastCategory

class PersonInline(admin.TabularInline):
    model = PersonMovie
    extra = 0

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_filter = ('genres',)
    search_fields = ('title', 'description')
    inlines = [PersonInline]

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('__str__',
                    'description',
                    'amount_movies')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(CastCategory)
class CastCategoryAdmin(admin.ModelAdmin):
    pass