from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField
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
class Categories(models.Model):
    Cat_Name = models.CharField(max_length=20,default=None,verbose_name="ชื่อแคท",help_text='This field is required.')
    Parent_ID = models.IntegerField(null=True)
    Cat_Level = models.IntegerField(null=True)
    Active  = models.BooleanField(default = True,help_text='This field is required.')
    Create_date = models.DateTimeField('Create Date',default=datetime.now(),null=False,help_text='This field is required.')
    create_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="UserXXX",help_text='This field is required.')
    updated_date = models.DateTimeField('Update Date', default=datetime.now(),null=False,help_text='This field is required.')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE,help_text='This field is required.')

    Test = models.CharField(max_length=20, default=None)
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
    Floor = models.CharField(max_length=10, choices=FLOOR_CHOICES, default=None, help_text='This field is required.')
    def save(self, *args, **kwargs):
        print("------------------Category save %s")
        if(self.FLOOR_CHOICES=='EMQ'):
            print("---EMQ")
        if (self.FLOOR_CHOICES == 'EMP'):
            print("---EMP")
        super(Category, self).save(*args, **kwargs)  # Call the "real" save()
    def __str__(self):
        return self.Cat_Name
class Shop(models.Model):
    SHOP_TYPE_CHOICE = (("Brand","Brand"),("Shop","Shop"))
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
    category = models.ForeignKey(Categories,related_name='shops', on_delete=models.CASCADE,default=6)
    Shop_ID = models.IntegerField(null=True)
    Shop_Name = models.CharField(null=True,max_length=200)
    Shop_ShortName_TH = models.CharField(max_length=200,null=True)
    Shop_ShortName_EN = models.CharField(max_length=200,null=True)
    Shop_Detail_TH = models. TextField(max_length=200,null=True)
    Shop_Detail_EN = models. TextField(max_length=200,null=True)
    Shop_type = models.CharField(max_length=20,choices=SHOP_TYPE_CHOICE,help_text='This field is required.')
    #*This field is required.
    #Cat_ID = models.CharField(max_length=10,choices=SHOP_TYPE_CHOICE,default=None)
    #cat_id = models.CharField(max_length=10, default=None)
    Active = models.BooleanField(default=True,help_text='This field is required.')
    icon = models.ImageField(default=None,help_text='This field is required.')
    cover = models.ImageField(default=None,help_text='This field is required.')
    Email = models.EmailField(null=True)
    Floor = models.CharField(max_length=10,choices=FLOOR_CHOICES, default=None,help_text='This field is required.')
    Tel = models.CharField(max_length=20,null=True)
    Branch_Code = models.CharField(max_length=4,choices=BRANCH_CHOICES, default=None,help_text='This field is required.')
    pivot_icon = models.CharField(null=True,max_length = 20)

    x_pivot = models.FloatField(default=0,null=True)
    y_pivot = models.FloatField(default=0,null=True)
    Create_date = models.DateTimeField('create date',default=None,null=False,help_text='This field is required.')
    Create_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="UserXXXX",help_text='This field is required.')
    Updated_date = models.DateTimeField('update date',default=None,null=False,help_text='This field is required.')
    Updated_by = models.ForeignKey(User, on_delete=models.CASCADE,help_text='This field is required.')
    def getCustomField(self,obj):
        return obj.y_pivot
    def __str__(self):
        return self.Shop_Name
    def save(self, *args, **kwargs):
        no = Shop.objects.count
        if (no == None):
            print('--------no objects')
            #self.Shop_ID = count
        else:
            count = Shop.objects.order_by('pk').last()
            last = 1
            if count == None:
                print('--------count is none')
                last = 1
            else:
                last = count.pk+1
                print('--------count is not none %s '%last)
            self.Shop_ID = last
        super(Shop, self).save(*args, **kwargs)  # Call the "real" save()
        self.Shop_ID = self.id
        ud = Shop.objects.get(pk=self.id)
        print('--------after save %s' % ud.Shop_ID)
        ud.Shop_ID = ud.pk
        Shop.objects.filter(id=self.id).update(Shop_ID=ud.id)
        #https://www.reddit.com/r/django/comments/3i31ka/how_do_i_get_an_auto_filled_and_auto_incrementing/
class Pic(models.Model):
    shop_pic = models.ImageField(upload_to='images')
    #shop_pic = models.ImageField(upload_to='uploads/', verbose_name='image')
#https://github.com/NiwatSriwilai/test_dj.git