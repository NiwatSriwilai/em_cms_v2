# Generated by Django 2.1.1 on 2019-02-04 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emcms', '0002_auto_20190204_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='Create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 14, 35, 8, 376105), help_text='This field is required.', verbose_name='Create Date'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 4, 14, 35, 8, 376105), help_text='This field is required.', verbose_name='Update Date'),
        ),
    ]
