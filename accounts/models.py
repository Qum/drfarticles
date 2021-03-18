from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import (PermissionsMixin, AbstractUser)
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _

from accounts.UserManager import UserManager


class User(AbstractUser):
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        blank=True,
    )
    email = models.EmailField(_('email address'), unique=True)
    phone_number = PhoneNumberField(blank=True)
    about = models.CharField(max_length=100, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'about', 'username', 'phone_number']
