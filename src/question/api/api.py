from rest_framework import viewsets
from .serializers import CharpterSerializers
from question import models


class CharpterViewSet(viewsets.ModelViewSet):
    queryset = models.Charpter.objects.filter(level=0)
    serializer_class = CharpterSerializers
