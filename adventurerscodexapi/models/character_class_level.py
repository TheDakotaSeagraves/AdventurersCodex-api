from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class CharacterClassLevel(models.Model):
    """Through model linking a Character to a DndClass with per-class level and subclass."""

    character = models.ForeignKey(
        "Character",
        on_delete=models.CASCADE,
        related_name="class_levels",
    )
    dnd_class = models.ForeignKey(
        "DndClass",
        on_delete=models.PROTECT,
    )
    level = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(20)],
    )
    subclass = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = [("character", "dnd_class")]

    def __str__(self):
        base = f"{self.dnd_class.name} {self.level}"
        return f"{base} ({self.subclass})" if self.subclass else base
