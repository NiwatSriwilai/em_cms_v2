# Generated by Django 2.1.1 on 2018-09-27 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pic',
            name='shop_pic',
            field=models.ImageField(upload_to='images'),
        ),
    ]