# Generated by Django 2.1.1 on 2018-10-31 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0028_auto_20181018_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='branch_code',
            field=models.CharField(choices=[('EMP', 'EMP'), ('EMQ', 'EMQ')], default=None, max_length=4),
        ),
    ]