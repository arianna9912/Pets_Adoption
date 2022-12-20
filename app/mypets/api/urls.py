from django.urls import path, include
from rest_framework import routers
from mypets.api.views import PetsViewSet,UserViewSet,AdoptionViewSet

router = routers.DefaultRouter()
router.register(r'pets', PetsViewSet, basename='pets')
router.register(r'user', UserViewSet, basename='user')
router.register(r'adopcion', AdoptionViewSet, basename='adopcion')




urlpatterns = [
    path('', include(router.urls)),
]
