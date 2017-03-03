from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Dvd(models.Model):
    name = models.CharField(max_length = 31)
    director = models.CharField(max_length = 31)
    release_date = models.IntegerField()
    slug = models.SlugField()
    genre = models.CharField(max_length=31)

    class Meta:
        unique_together = (('slug','name'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dvd_detail', kwargs={'slug':self.slug})
    def get_update_url(self):
        return reverse('dvd_update',
                       kwargs={'slug': self.slug})
    def get_delete_url(self):
        return reverse('dvd_delete',
                       kwargs={'slug': self.slug})


class Book(models.Model):
    name = models.CharField(max_length = 31)
    author = models.CharField(max_length = 31)
    slug = models.SlugField()
    genre = models.CharField(max_length=31)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('book_detail', kwargs={'slug':self.slug})
    def get_update_url(self):
        return reverse('book_update',
                       kwargs={'slug': self.slug})
    def get_delete_url(self):
        return reverse('book_delete',
                        kwargs={'slug': self.slug})

class Music(models.Model):
    name = models.CharField(max_length = 31)
    artist = models.CharField(max_length = 31)
    release_date = models.DateField()
    slug = models.SlugField()
    genre = models.CharField(max_length=31)
    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=31)
    movies = models.ManyToManyField(Dvd)
    def __str__(self):
        return self.name
