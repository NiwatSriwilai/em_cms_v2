from django.db import models

# Create your models here.
#db command
#-python manage.py makemigrations polls
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)