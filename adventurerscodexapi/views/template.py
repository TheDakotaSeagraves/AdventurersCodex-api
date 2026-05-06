
from django.http import HttpResponseServerError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rockapi.models import Void


class TemplateView(ViewSet):
    """Void view set"""


    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized instance
        """
        void = Void()
        void.sample_name = request.data["name"]
        void.sample_description = request.data["description"]

        try:
            void.save()
            serializer = VoidSerializer(void)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single item

        Returns:
            Response -- JSON serialized instance
        """
        try:
            void = Void.objects.get(pk=pk)
            serializer = VoidSerializer(void)
            return Response(serializer.data)
        except Exception as ex:
            return Response({"reason": ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handle PUT requests

        Returns:
            Response -- Empty body with 204 status code
        """
        try:
            void = Void.objects.get(pk=pk)
            void.sample_name = request.data["name"]
            void.sample_description = request.data["description"]
            void.save()
        except Void.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return HttpResponseServerError(ex)

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single item

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            void = Void.objects.get(pk=pk)
            void.delete()
            return Response(None, status=status.HTTP_204_NO_CONTENT)

        except Void.DoesNotExist as ex:
            return Response({message: ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({message: ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests for all items

        Returns:
            Response -- JSON serialized array
        """
        try:
            voids = Void.objects.all()
            serializer = VoidSerializer(voids, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)


class VoidSerializer(serializers.ModelSerializer):
    """JSON serializer"""

    class Meta:
        model = Void
        fields = ( id, sample_name, sample_description, )

