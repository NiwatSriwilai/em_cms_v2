from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
#db command
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver
class Category(models.Model):
    name = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name
class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    shop_name = models.CharField(max_length=200)
    shop_shortname_th = models.CharField(max_length=200,null=True)
    shop_shortname_en = models.CharField(max_length=200,null=True)
    shop_details_th = models.CharField(max_length=200,null=True)
    shop_details_en = models.CharField(max_length=200,null=True)
    shop_type = models.CharField(max_length=10,default=None)
    #cat_id = models.CharField(max_length=10, default=None)
    active = models.CharField(max_length=100, default=None)
    icon = models.ImageField(default=None)
    cover = models.ImageField(default=None)
    email = models.EmailField(null=True)
    floor = models.CharField(max_length=10, default=None)
    tel = PhoneNumberField(default=None)
    branch_code = models.CharField(max_length=4, default=None)
    pivot_icon = models.ImageField(null=True)
    x_pivot = models.FloatField(default=0)
    y_pivot = models.FloatField(default=0)
    create_date = models.DateTimeField('create date',default=None)
    create_by = models.CharField(max_length=50, default=None)
    updated_date = models.DateTimeField('update date',default=None)
    updated_by = models.CharField(max_length=50, default=None)
    def __str__(self):
            return str(self.shop_name)
class Pic(models.Model):
    shop_pic = models.ImageField(upload_to='images')

#https://github.com/NiwatSriwilai/test_dj.git