from django.db import models

# Create your models here.
class VictimSurvivorInformation(models.Model):
    CIVIL_STATUS_CHOICES = [
        ('SINGLE', 'Single'),
        ('MARRIED', 'Married'),
        ('WIDOWED', 'Widowed'),
        ('SEPARATED', 'Separated'),
        ('DIVORCED', 'Divorced'),
    ]

    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    # sex
    birthDate = models.DateField()
    placeOfBirth = models.CharField(max_length=100)
    isMinor = models.BooleanField(default=False)
    civilStatus = models.CharField(max_length=50, choices=CIVIL_STATUS_CHOICES, default='SINGLE')
    # nationality
    occupation = models.CharField(max_length=100, blank=True, null=True)
    monthlyIncome = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employmentStatus = models.CharField(max_length=50, blank=True, null=True)
    migratoryStatus = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    currentAddress = models.CharField(max_length=255)
    isDisplaced = models.BooleanField(default=False)
    isPWD = models.BooleanField(default=False)
    contactNumber = models.CharField(max_length=15, blank=True, null=True)