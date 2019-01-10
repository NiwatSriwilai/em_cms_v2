from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from mysite import settings
from datetime import datetime
#from rest_framework import serializers
from django_userforeignkey.models.fields import UserForeignKey
# Create your models here.
#db command
#python manage.py makemigrations
#python manage.py migrate
#python manage.py runserver
#a = User.objects.get(pk=2)
#print('------data = %s'%a.username)
class Category(models.Model):
    Cat_Name = models.CharField(max_length=20,default=None)
    Parent_ID = models.IntegerField(max_length=4,null=True)
    Cat_Level = models.IntegerField(max_length=4,null=True)
    Active  = models.BooleanField(default = True)
    Create_date = models.DateTimeField('Create Date',default=datetime.now(),null=False)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="UserXXX")
    updated_date = models.DateTimeField('Update Date', default=datetime.now(),null=False)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Cat_Name
class Shop(models.Model):
    SHOP_TYPE_CHOICE = (("1","1"),("2","2"))
    BRANCH_CHOICES = (("EMP","EMP"),("EMQ","EMQ"))
    FLOOR_CHOICES = (
        ('EMP', (
            ('Floo1', 'Floo1'),
            ('M', 'M'),
        )
         ),
        ('EMQ', (
            ('G', 'G'),
            ('Floo1', 'Floo1'),
            ('M', 'M')
        )
        )
    )
    category = models.ForeignKey(Category,related_name='shops', on_delete=models.CASCADE,default=6)
    Shop_ID = models.IntegerField(default=1)
    Shop_Name = models.CharField(max_length=200)
    Shop_ShortName_TH = models.CharField(max_length=200,null=True)
    Shop_ShortName_EN = models.CharField(max_length=200,null=True)
    Shop_Detail_TH = models.CharField(max_length=200,null=True)
    Shop_Detail_EN = models.CharField(max_length=200,null=True)
    Cat_ID = models.CharField(max_length=10,choices=SHOP_TYPE_CHOICE,default=None)
    #cat_id = models.CharField(max_length=10, default=None)
    Active = models.CharField(max_length=100, default=None)
    icon = models.ImageField(default=None)
    cover = models.ImageField(default=None)
    Email = models.EmailField(null=True)
    Floor = models.CharField(max_length=10,choices=FLOOR_CHOICES, default=None)
    Tel = PhoneNumberField(default=None)
    Branch_Code = models.CharField(max_length=4,choices=BRANCH_CHOICES, default=None)
    pivot_icon = models.ImageField(null=True)
    x_pivot = models.FloatField(default=0)
    y_pivot = models.FloatField(default=0)
    Create_date = models.DateTimeField('create date',default=None,null=False)
    Create_by = models.CharField(max_length=200,null=False)
    Updated_date = models.DateTimeField('update date',default=None,null=False)
    Updated_by = models.CharField(max_length=200,null=False)

    def __str__(self):
        return self.Shop_Name
class Pic(models.Model):
    shop_pic = models.ImageField(upload_to='images')
    #shop_pic = models.ImageField(upload_to='uploads/', verbose_name='image')
#https://github.com/NiwatSriwilai/test_dj.git