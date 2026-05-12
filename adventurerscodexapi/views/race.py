"""Race API — read-only endpoints for listing and retrieving races."""

from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated

from adventurerscodexapi.models import Race


class RaceSerializer(serializers.ModelSerializer):
    """Serializes Race instances. Exposes all four model fields."""

    class Meta:
        model = Race
        fields = ["id", "name", "description", "is_homebrew", "created_by"]


class RaceViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoint for races. Auth required; write methods return 405."""

    queryset = Race.objects.all()
    serializer_class = RaceSerializer
    permission_classes = [IsAuthenticated]
