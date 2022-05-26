from rest_framework import viewsets

from myapi.serializers import MonsterSerializer
from myapi.models import Monster

class MonsterViewSet(viewsets.ModelViewSet):
    serializer_class = MonsterSerializer
    queryset = Monster.objects.all()
