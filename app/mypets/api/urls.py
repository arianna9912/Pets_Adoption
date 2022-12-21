from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from mypets.api.views import PetsViewSet,UserViewSet,AdoptionViewSet
from mypets.api.authentication import Login,Logout

router = routers.DefaultRouter()
router.register(r'pets', PetsViewSet, basename='pets')
router.register(r'user', UserViewSet, basename='user')
router.register(r'adopcion', AdoptionViewSet, basename='adopcion')





urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]



