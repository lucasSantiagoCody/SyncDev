from django.db import models
from django.contrib.auth.models import AbstractUser
 
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=40)
    username = models.CharField(unique=False, max_length=30)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    def __str__(self) -> str:
        return self.username
 
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.FileField(upload_to='profile_pictures', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    nif = models.CharField(max_length=14, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.user.username
