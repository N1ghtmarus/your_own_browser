from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя"""
    REQUIRED_FIELDS = [
        'email',
    ]
    email = models.EmailField(
        blank=False,
        max_length=254,
        unique=True
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
