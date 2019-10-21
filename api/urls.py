
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restaurantes.api.viewset import RestauranteViewSet
from menus.api.viewset import MenuViewSet
from reviews.api.viewset import ReviewViewSet



router = routers.DefaultRouter()
router.register(r'restaurantes', RestauranteViewSet, basename='Restaurante')
router.register(r'menus', MenuViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
