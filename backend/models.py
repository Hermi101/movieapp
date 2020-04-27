from django.db import models

# Create your models here.
# Comment

class Movie(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    duration = models.IntegerField()
    cover = models.TextField(blank=True)
    trailer_url = models.URLField(blank=True)

    #N.M Relation -> zwischen-Tabelle wird automatisch erstellt
    genres = models.ManyToManyField('Genre',
                                    related_name='movies')
    people = models.ManyToManyField('Person',
                                    through='PersonMovie',
                                    related_name='movies')
    cast = models.ManyToManyField('CastCategory',
                                 through='PersonMovie',
                                 related_name='castcategory')

    def __str__(self):
        return self.title

class Genre(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def amount_movies(self):
        """
        return count of my Movies
        """
        return self.movies.count()


class Person(models.Model):
    name = models.CharField(max_length=256, help_text='Firstname Lastname')
    geb_date = models.DateField()

    def __str__(self):
        return self.name

class PersonMovie(models.Model):
    cast = models.ForeignKey('CastCategory',
                             on_delete=models.CASCADE)

    movie = models.ForeignKey('Movie',
                              on_delete=models.CASCADE)
    person = models.ForeignKey('Person',
                              on_delete=models.CASCADE)


class CastCategory(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    def __str__(self):
        return self.name
