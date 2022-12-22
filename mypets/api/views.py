from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from mypets.api.serializer import PetsSerializer, UserSerializer, AdoptionSerializer
from mypets.models import Pets, Adoption


class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = PetsSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AdoptionViewSet(ModelViewSet):
    queryset = Adoption.objects.all()
    serializer_class = AdoptionSerializer
