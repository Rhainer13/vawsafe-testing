from django.db import models

SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

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
    # extension = models.CharField(max_length=10, blank=True, null=True)
    # sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    # isSOGIE = models.BooleanField(default=False)
    # birthDate = models.DateField()
    # placeOfBirth = models.CharField(max_length=100)

    # if victim is minor, name and contact info of parent/guardian
    # isMinor = models.BooleanField(default=False)

    # civilStatus = models.CharField(max_length=50, choices=CIVIL_STATUS_CHOICES, default='SINGLE')
    # nationality
    # ethnicity = models.CharField(max_length=50, blank=True, null=True)
    # mainOccupation = models.CharField(max_length=100, blank=True, null=True)
    # monthlyIncome = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    # employmentStatus = models.CharField(max_length=50, blank=True, null=True)
    # migratoryStatus = models.CharField(max_length=50, blank=True, null=True)
    # religion = models.CharField(max_length=50, blank=True, null=True)
    # currentAddress = models.CharField(max_length=255)
    # isDisplaced = models.BooleanField(default=False)
    # isPWD = models.BooleanField(default=False)
    # contactNumber = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.lastName

class IncidentInformation(models.Model):
    TYPE_OF_PLACE = [
        ('Conjugal Home', 'Conjugal Home'),
        ('Evacutaion Area', 'Evacutaion Area'),
        ('Malls/Hotels', 'Malls/Hotels'),
        ('Perpetrator\'s Home', 'Perpetrator\'s Home'),
        ('Public Utility Vehicle', 'Public Utility Vehicle'),
        ('Victim\'s Home', 'Victim\'s Home'),
        ('Workplace', 'Workplace'),
    ]

    victimSurvivor = models.ForeignKey(VictimSurvivorInformation, on_delete=models.CASCADE)
    # violenceType = models.CharField(max_length=100)
    description = models.TextField()
    # incidentDate = models.DateField()
    # incidentTime = models.TimeField()
    # incidentLocation = models.CharField(max_length=255)
    # typeOfPlace = models.CharField(max_length=50, choices=TYPE_OF_PLACE)
    # isViaElectronicMeans = models.BooleanField(default=False)
    # isResultOfHarmfulPractice = models.BooleanField(default=False)
    # isConflictArea = models.BooleanField(default=False)
    # isCalamityArea = models.BooleanField(default=False)

class AllegedPerpetratorInformation(models.Model):
    victimSurvivor = models.ForeignKey(VictimSurvivorInformation, on_delete=models.CASCADE)
    lastName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100, blank=True, null=True)
    # sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    # birthdate = models.DateField()
    # birthPlace = models.CharField(max_length=100)

    # if perpetrator is minor, name and contact info of parent/guardian
    # parentGuardianName = models.CharField(max_length=100, blank=True, null=True)

    # nationality = models.CharField(max_length=50)
    # mainOccupation = models.CharField(max_length=100, blank=True, null=True)
    # religion = models.CharField(max_length=50, blank=True, null=True)
    # address
    # victimRelationship = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.lastName