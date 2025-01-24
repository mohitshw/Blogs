from django.db import models
from django.contrib.auth.models import AbstractUser
import re

class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_created_at = models.DateTimeField(null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

    def validate_username(self, username):
        # Username can only contain numbers and characters
        if not re.match(r'^[a-zA-Z0-9]+$', username):
            raise ValueError("Username must contain only letters and numbers")

    def save(self, *args, **kwargs):
        # Skip username validation for temporary usernames
        if not self.username.startswith('temp_'):
            self.validate_username(self.username)
        super().save(*args, **kwargs)