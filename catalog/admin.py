from django.contrib import admin
from .models import Dvd, Book
# Register your models here.

class DvdAdmin(admin.ModelAdmin):
    pass

admin.site.register(Dvd)
admin.site.register(Book)
