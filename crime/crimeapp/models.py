from django.db import models

# Create your models here.


class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    MARITAL_STATUS_CHOICES = [
        ('single', 'Single'),
        ('married', 'Married'),
    ]

    username = models.CharField(max_length=255, unique=True)
    # password = models.CharField(max_length=100, null=True, blank=True) 
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20,blank=True,null=True)  
    status = models.CharField(max_length=10, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.CharField(max_length=10)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.username

class Location(models.Model):
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,blank=True,null=True)

    def __str__(self):
        return f"{self.city}, {self.address}"


class CrimeType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crime_type = models.ForeignKey(CrimeType, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    date_reported = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"Report #{self.id} by {self.user.username}"
