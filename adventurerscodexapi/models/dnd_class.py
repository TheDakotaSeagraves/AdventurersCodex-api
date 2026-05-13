from django.db import models


class DndClass(models.Model):
    """A D&D character class definition (Fighter, Wizard, etc.)."""

    name = models.CharField(max_length=50, default="")
    hit_die = models.CharField(max_length=5, default="")
    primary_ability = models.CharField(max_length=100, default="")
    saving_throw_proficiencies = models.CharField(max_length=100, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.name
