from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):  # models.Model을 상속

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LENGUAGE_ENGLISH = "en"
    LENGUAGE_KOREAN = "kr"

    LENGUAGE_CHOICES = (
        (LENGUAGE_ENGLISH, "English"),
        (LENGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "Usd"),
        (CURRENCY_KRW, "Krw"),
    )

    avatar = models.ImageField(upload_to="avatars", blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)

    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)

    language = models.CharField(choices=LENGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)

    superhost = models.BooleanField(default=False)
