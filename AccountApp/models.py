from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator , MaxLengthValidator ,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
class Speciality(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Speciality"
        verbose_name_plural="Specialities"
   
# Create your models here.
class User(AbstractUser):
    pass

class Doctor(User):
    licence_number = models.CharField(max_length=6,unique=True,validators= [MinLengthValidator(6), MaxLengthValidator(6)])
    phone=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    specialities=models.ManyToManyField(
        Speciality,
        related_name="doctors"
    )
    class Meta:
            verbose_name="Doctor"
            verbose_name_plural="Doctors"
number_Validator=RegexValidator(
        regex= r'^\d{8}$',
        message="le numero incorrect, ne respecte pas le pattern 8 chiffres exacte"
    )
def validate_birth_date(v):
    if v>= timezone.localdate():
        raise ValidationError("la date de naissance  doit etre inferieur a la date d'aujordhui")
class Patient(User):
    national_id=models.CharField(max_length=8,unique=True,validators=[number_Validator])
    phone=models.CharField(max_length=8,validators=[number_Validator])
    birth_date=models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    class Meta:
            verbose_name="Patient"
            verbose_name_plural="Patients"
