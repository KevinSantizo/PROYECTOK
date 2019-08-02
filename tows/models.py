from django.db import models
from django.urls import reverse

# Create your models here.


class Crane(models.Model):
    license_plate = models.CharField(max_length=50)
    trademark = models.CharField(max_length=50)
    year = models.IntegerField()
    characteristic = models.CharField(max_length=100)

    def __str__(self):
        return self.trademark + ' -- ' + self.characteristic


class Pilot(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    DPI = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name + '  ' + self.last_name


class Assignment(models.Model):
    LOAN_STATUS = (
        ('O', 'On Route'),
        ('A', 'Available'),
    )
    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default='O',
        help_text='Crane availability',
    )
    start_time = models.DateTimeField()
    pilot_assigned = models.ForeignKey(Pilot, on_delete=models.CASCADE, null=True)
    crane_assigned = models.ForeignKey(Crane, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.status + ' Pilot: ' + self.pilot_assigned.first_name + ' Crane: ' + self.crane_assigned.license_plate



