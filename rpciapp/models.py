from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    # Add other fields as needed

    def __str__(self):
        return self.user.username
