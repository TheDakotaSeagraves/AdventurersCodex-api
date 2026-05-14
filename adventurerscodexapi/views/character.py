from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from adventurerscodexapi.models import Character, DndClass, Race

from .dnd_class import DndClassSerializer
from .race import RaceSerializer


class CharacterSerializer(serializers.ModelSerializer):
    """Serializer for Character with nested Race/DndClass on read and ID fields on write."""

    user = serializers.PrimaryKeyRelatedField(read_only=True)
    race = RaceSerializer(read_only=True)
    dnd_class = DndClassSerializer(read_only=True)
    race_id = serializers.PrimaryKeyRelatedField(
        queryset=Race.objects.all(), source="race", write_only=True
    )
    dnd_class_id = serializers.PrimaryKeyRelatedField(
        queryset=DndClass.objects.all(), source="dnd_class", write_only=True
    )

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "user",
            "race",
            "race_id",
            "dnd_class",
            "dnd_class_id",
            "level",
            "strength",
            "dexterity",
            "constitution",
            "intelligence",
            "wisdom",
            "charisma",
            "armor_class",
            "hp_max",
            "hp_current",
            "background",
            "alignment",
            "backstory",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "background": {"required": False, "allow_blank": True},
            "alignment": {"required": False, "allow_blank": True},
            "backstory": {"required": False, "allow_blank": True},
        }


class CharacterViewSet(viewsets.ModelViewSet):
    """CRUD endpoint scoped to the requesting user's characters."""

    serializer_class = CharacterSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Character.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
