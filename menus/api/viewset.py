from django.shortcuts import render
from rest_framework import viewsets
from menus.models import Menu
from menus.api.serializers import MenuSerializer

class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
 #   lookup_field='slug'

    serializer_class = MenuSerializer
    filterset_fields = ['restaurantId']