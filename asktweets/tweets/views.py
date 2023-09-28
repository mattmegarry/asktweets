from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MP
from .serializers import MPSerializer

class ListMPs(APIView):
    def get(self, request, format=None):
        MPs = MP.objects.all()
        serializer = MPSerializer(MPs, many=True)
        return Response(serializer.data)