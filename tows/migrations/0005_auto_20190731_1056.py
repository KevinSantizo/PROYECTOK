# Generated by Django 2.2.3 on 2019-07-31 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tows', '0004_auto_20190731_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='status',
            field=models.CharField(blank=True, choices=[('O', 'On Route'), ('A', 'Available')], default='O', help_text='Crane availability', max_length=1),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='DPI',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='pilot',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]