"""Race model — represents a D&D race assignable to a Character."""

from django.conf import settings
from django.db import models


class Race(models.Model):
    """A D&D race. SRD races have created_by=None; homebrew races are user-created."""

    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=20, default="")
    speed = models.CharField(max_length=30, default="")
    ability_score_increases = models.CharField(max_length=200, default="")
    traits = models.TextField(default="")
    languages = models.CharField(max_length=200, default="")
    is_homebrew = models.BooleanField(default=False)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="homebrew_races",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        """Display the race's name."""
        return self.name
