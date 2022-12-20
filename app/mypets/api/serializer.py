from rest_framework import serializers
from django.contrib.auth.models import User
from mypets.models import *


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdoptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adoption
        fields = '__all__'


