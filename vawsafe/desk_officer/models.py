from django.db import models

SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

RELIGION_CHOICES = [
        ('Roman Catholic', 'Roman Catholic'),
        ('Islam', 'Islam'),
        ('Evangelicals', 'Evangelicals'),
        ('Protestant', 'Protestant'),
        ('Iglesia ni Cristo', 'Iglesia ni Cristo'),
        ('Others', 'Others'),
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

    SOGIE_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Does not want to identify', 'Does not want to identify'),
    ]

    EDUCATIONAL_ATTAINMENT_CHOICES = [
        ('No Formal Education', 'No Formal Education'),
        ('Elementary Level/Graduate', 'Elementary Level/Graduate'),
        ('Junior High School Level/Graduate', 'Junior High School Level/Graduate'),
        ('Senior High School Level/Graduate', 'Senior High School Level/Graduate'),
        ('Technical/Vocational', 'Technical/Vocational'),
        ('College Level/Graduate', 'College Level/Graduate'),
        ('Post graduate', 'Post graduate'),
    ]

    NATIONALITY_CHOICES = [
        ('Filipino', 'Filipino'),
        ('Others', 'Others'),
    ]

    EMPLOYMENT_STATUS_CHOICES = [
        ('Employed', 'Employed'),
        ('Self-employed', 'Self-employed'),
        ('Unemployed', 'Unemployed'),
        ('Informal Sector', 'Informal Sector'),
        ('Not Applicable', 'Not Applicable'),
    ]

    MIGRATORY_STATUS_CHOICES = [
        ('Current OFW', 'Current OFW'),
        ('Former/Returning OFW', 'Former/Returning OFW'),
        ('Seeking employment abroad', 'Seeking employment abroad'),
        ('Not Applicable', 'Not Applicable'),
    ]

    PWD_CHOICES = [
        ('None', 'None'),
        ('Deaf or Hard of Hearing', 'Deaf or Hard of Hearing'),
        ('Intellectual Disability', 'Intellectual Disability'),
        ('Learning DIsability', 'Learning DIsability'),
        ('Mental Disability', 'Menatl Disability'),
        ('Orthopedic Disability', 'Orthopedic Disability'),
        ('Physical Disability', 'Physical Disability'),
        ('Psychological Disability', 'Psychological Disability'),
        ('Speech and Language Disability', 'Speech and Language Disability'),
        ('Visual Disability', 'Visual Disability'),
    ]

    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=10, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    is_SOGIE = models.CharField(max_length=50, choices=SOGIE_CHOICES, default='No')
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)

    # if victim is minor, name and contact info of parent/guardian
    # isMinor = models.BooleanField(default=False)

    civil_status = models.CharField(max_length=50, choices=CIVIL_STATUS_CHOICES, default='SINGLE')
    educational_attainment = models.CharField(max_length=50, choices=EDUCATIONAL_ATTAINMENT_CHOICES, default='No Formal Education')
    nationality = models.CharField(max_length=50, choices=NATIONALITY_CHOICES, default='Filipino')
    ethnicity = models.CharField(max_length=50, blank=True, null=True)
    main_occupation = models.CharField(max_length=100, blank=True, null=True)
    monthly_income = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    employment_status = models.CharField(max_length=50, choices=EMPLOYMENT_STATUS_CHOICES, default='Not Applicable')
    migratory_status = models.CharField(max_length=50, choices=MIGRATORY_STATUS_CHOICES, default='Not Applicable')
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, default='Roman Catholic')
    # currentAddress = models.CharField(max_length=255)
    is_displaced = models.BooleanField(default=False)
    PWD_type = models.CharField(max_length=50, choices=PWD_CHOICES, default='None')
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.last_name

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

    CONFLICT_AREA_CHOICES = [
        ('Insurgency', 'Insurgency'),
        ('Violent Extremism', 'Violent Extremism'),
        ('Tribal Violence', 'Tribal Violence'),
        ('Political Violence', 'Political Violence'),
        ('Rido', 'Rido'),
        ('Others', 'Others'),
    ]

    victim_survivor = models.ForeignKey(VictimSurvivorInformation, on_delete=models.CASCADE)
    # violenceType = models.CharField(max_length=100)
    description = models.TextField()
    incident_date = models.DateField()
    incident_time = models.TimeField()
    incident_location = models.CharField(max_length=255, blank=True, null=True)
    type_of_place = models.CharField(max_length=50, choices=TYPE_OF_PLACE)
    # isViaElectronicMeans = models.BooleanField(default=False)
    # isResultOfHarmfulPractice = models.BooleanField(default=False)
    is_conflict_area = models.BooleanField(default=False)
    conflict_area = models.CharField(max_length=50, choices=CONFLICT_AREA_CHOICES, blank=True, null=True)
    is_calamity_area = models.BooleanField(default=False)

class AllegedPerpetratorInformation(models.Model):
    victim_survivor = models.ForeignKey(VictimSurvivorInformation, on_delete=models.CASCADE)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES)
    birth_date = models.DateField()
    birth_place = models.CharField(max_length=100)

    # if perpetrator is minor, name and contact info of parent/guardian
    # parentGuardianName = models.CharField(max_length=100, blank=True, null=True)

    # nationality = models.CharField(max_length=50)
    main_occupation = models.CharField(max_length=100, blank=True, null=True)
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, default='Roman Catholic')
    # address
    # victimRelationship = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.last_name