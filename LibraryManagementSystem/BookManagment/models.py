from django.db import models
from django.utils import timezone

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    
    class Status(models.TextChoices):
# on this part, link it to borrow to say borrowed or avilable.
    
        AVAILABLE = 'available', 'Available'
        BORROWED = 'borrowed', 'Borrowed'
    
    
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AVAILABLE)
    created_time = models.DateTimeField(default = timezone.now )
    def __str__(self):
        return self.title
