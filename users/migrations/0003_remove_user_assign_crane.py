# Generated by Django 2.2.3 on 2019-07-31 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190730_1522'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='assign_crane',
        ),
    ]
