from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import models

from .models import NewsStory

# Register your models here.

admin.site.register(NewsStory)