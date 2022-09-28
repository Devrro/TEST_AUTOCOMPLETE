from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .managers import UserManager


class UserModel(AbstractBaseUser):
    class Meta:
        db_table = 'users'

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()


class ProfileModel(models.Model):
    class Meta:
        db_table = 'profile'

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=16)
    age = models.IntegerField(validators=[MaxValueValidator(122), MinValueValidator(0)])
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
    # profile_picture = models.ImageField(upload_to=upload_picture_to, blank=True)
    is_medic = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=True)
