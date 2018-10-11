from django.db import models

# Create your models here.
#db command
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver
class Category(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200)
    def __str__(self):
        return self.shop_name
class Pic(models.Model):
    shop_pic = models.ImageField(upload_to='images')

#https://github.com/NiwatSriwilai/test_dj.git