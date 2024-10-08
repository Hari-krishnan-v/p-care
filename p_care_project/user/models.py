from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.apps import apps
from doctor.models import Hospital


TREATMENT_CHOICES = [
    ('grooming', 'Grooming'),
    ('medical', 'Medical'),
    ('vaccination', 'Vaccination'),
    ('surgery', 'Surgery'),
    # Add more treatment types as needed
]

class PetProfile(models.Model):
    PET_TYPES = [
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('bird', 'Bird'),
        # Add more pet types as needed
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pet_name = models.CharField(max_length=100)
    pet_birthdate = models.DateField()
    pet_type = models.CharField(max_length=10, choices=PET_TYPES)

    def __str__(self):
        return f"{self.pet_name} ({self.pet_type})"

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_profile = models.ForeignKey('user.PetProfile', on_delete=models.CASCADE, default=1)  # Set default here
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    treatment_type = models.CharField(max_length=20, choices=TREATMENT_CHOICES)
    hospital = models.ForeignKey('doctor.Hospital', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    scheduled_date = models.DateTimeField(default=timezone.now)
    sent_date = models.DateField(default=timezone.now)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
       return f'Appointment with {self.hospital} on {self.scheduled_date}'

    class Meta:
        ordering = ["-sent_date"]

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthdate = models.DateField()

    def __str__(self):
        return self.user.username

class Vaccination(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    next_vaccination_date = models.DateField()
    due_date = models.DateField()
    vaccine_name = models.CharField(max_length=100)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Vaccination for {self.user.username} on {self.next_vaccination_date}"
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.user.username}'
