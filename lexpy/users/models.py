from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


def user_directory_path(instance, filename):
    #file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.username, filename)


class User(AbstractUser):
    EXPERIENCE_BEGINNER = 'B'
    EXPERIENCE_BEGINT = 'BI'
    EXPERIENCE_INTERMEDIATE = 'I'
    EXPERIENCE_INTERVANCED = 'IA'
    EXPERIENCE_ADVANCED = 'A'
    DOMAIN_WEB_DEVELOPMENT = 'WD'
    DOMAIN_SCIENTIFIC_AND_NUMERIC = 'SN'
    DOMAIN_EDUCATION = 'E'
    DOMAIN_DESKTOP_GUIS = 'DG'
    DOMAIN_GAME_DEVELOPMENT = 'GD'
    DOMAIN_SOFTWARE_DEVELOPMENT = 'SD'
    DOMAIN_SCRIPTING = 'S'

    EXPERIENCE_CHOICES = (
        (EXPERIENCE_BEGINNER, 'Beginner'),
        (EXPERIENCE_BEGINT, 'Beginner to Intermediate'),
        (EXPERIENCE_INTERMEDIATE, 'Intermediate'),
        (EXPERIENCE_INTERVANCED, 'Intermediate to Advanced'),
        (EXPERIENCE_ADVANCED, 'Advanced / Professional'),
        )

    DOMAIN_CHOICES = (
        (DOMAIN_WEB_DEVELOPMENT, "Web Applications"),
        (DOMAIN_SCIENTIFIC_AND_NUMERIC, "Scientific or Numeric Applications"),
        (DOMAIN_EDUCATION, "Education"),
        (DOMAIN_DESKTOP_GUIS, "Desktop Software (GUI's)"),
        (DOMAIN_GAME_DEVELOPMENT, "Game Development"),
        (DOMAIN_SOFTWARE_DEVELOPMENT, "Support Software"),
        (DOMAIN_SCRIPTING, "Scripting"),
        )

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    photo = models.ImageField(upload_to=user_directory_path,
            blank=True,
            width_field="width_field",
            height_field="height_field")
    height_field = models.IntegerField(default=0, blank= True, null=True)
    width_field = models.IntegerField(default=0, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=2, choices=EXPERIENCE_CHOICES, blank=True, null=True)
    domain = models.CharField(max_length=2, choices=DOMAIN_CHOICES, blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
