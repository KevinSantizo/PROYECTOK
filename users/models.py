from django.db import models
from tows.models import Crane
# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100, help_text='Enter your name')
    last_name = models.CharField(max_length=100, help_text='Enter your last name')
    address = models.CharField(max_length=100, help_text='Describe your Company Address')
    phone = models.CharField(max_length=8, help_text='Enter Company Phone')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50, help_text='Enter your password')

    def __str__(self):
        return self.first_name + ' --- ' + self.last_name
