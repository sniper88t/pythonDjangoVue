from rest_framework import viewsets
from .models import mainStart
from .serializers import mainStartSerializer
class mainStartViewSet(viewsets.ModelViewSet):
    queryset = mainStart.objects.all()
    serializer_class = mainStartSerializer