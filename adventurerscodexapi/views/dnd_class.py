from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from adventurerscodexapi.models import DndClass


class DndClassSerializer(serializers.ModelSerializer):
    """Serializer for the DndClass model."""

    class Meta:
        model = DndClass
        fields = [
            "id",
            "name",
            "hit_die",
            "primary_ability",
            "saving_throw_proficiencies",
            "description",
        ]


class DndClassViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only viewset exposing DndClass list and detail endpoints."""

    queryset = DndClass.objects.all()
    serializer_class = DndClassSerializer
    permission_classes = [IsAuthenticated]
