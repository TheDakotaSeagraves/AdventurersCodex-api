from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .race import Race


class Character(models.Model):
    """A player character belonging to a single user."""

    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="characters")
    race = models.ForeignKey(Race, on_delete=models.PROTECT, related_name="characters")
    strength = models.IntegerField(
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    dexterity = models.IntegerField(
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    constitution = models.IntegerField(
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    intelligence = models.IntegerField(
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    wisdom = models.IntegerField(
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    charisma = models.IntegerField(
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
    )
    armor_class = models.IntegerField(default=10)
    hp_max = models.IntegerField(default=1)
    hp_current = models.IntegerField(default=1)
    background = models.CharField(max_length=100, default="")
    alignment = models.CharField(max_length=100, default="")
    backstory = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
