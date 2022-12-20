from rest_framework.viewsets import ModelViewSet
from mypets.api.serializer import *
from mypets.models import *
from django.db.models import Q

class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdoptionViewSet(ModelViewSet):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer

