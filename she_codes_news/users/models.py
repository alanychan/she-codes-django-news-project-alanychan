from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    bio_content = models.TextField(blank=True, null=True)
    photo_url = models.URLField(blank=True)
    pass

    def __str__(self):
        return self.username