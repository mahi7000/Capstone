from django.contrib import admin
from .models import Book

admin.site.register(Book)
admin.site.site_header=('welcome to Book Management !!!')
