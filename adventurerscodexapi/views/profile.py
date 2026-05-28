from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class ProfileSerializer(serializers.ModelSerializer):
    """Serializes the authenticated user's profile data."""

    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="last_name")
    dateJoined = serializers.DateTimeField(source="date_joined", read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "firstName",
            "lastName",
            "dateJoined",
        )


@api_view(["GET", "PUT"])
@permission_classes([IsAuthenticated])
def profile(request):
    """Handles fetching and updating the authenticated user's profile.

    GET: Returns the current user's profile data.
    PUT: Updates username, email, first_name, last_name, and optionally password.
    """
    user = request.user

    if request.method == "GET":
        serializer = ProfileSerializer(user)
        return Response(serializer.data)

    # PUT
    serializer = ProfileSerializer(user, data=request.data, partial=True)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()

    # Handle optional password change separately since it requires hashing
    new_password = request.data.get("password")
    if new_password:
        user.set_password(new_password)
        user.save()

    return Response(serializer.data)
