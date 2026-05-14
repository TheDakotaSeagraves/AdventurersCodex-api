"""Django admin registrations for The Adventurer's Codex models."""

from django.contrib import admin

from .models import Character, DndClass, Race

admin.site.register(Character)
admin.site.register(DndClass)
admin.site.register(Race)
