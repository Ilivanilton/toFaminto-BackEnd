from django.shortcuts import render
from django.core import serializers

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter


from restaurantes.models import Restaurante
from restaurantes.api.serializers import RestauranteSerializer

class RestauranteViewSet(ModelViewSet):

    serializer_class = RestauranteSerializer
  #  lookup_field='slug'
#    filterset_fields = ['slug']
#    filter_backends = [SearchFilter]
#    search_fields = ['slug']

    def get_queryset(self):
        return Restaurante.objects.all()
    
    def list(self, request, *args, **kwargs):
        return super(RestauranteViewSet,self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(RestauranteViewSet,self).create(request, *args, **kwargs)
    
    
    def destroy(self, request, *args, **kwargs):
        return super(RestauranteViewSet,self).destroy(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super(RestauranteViewSet,self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(RestauranteViewSet,self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super(RestauranteViewSet,self).partial_update(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def menu(self, request, slug=None):
        qs = Restaurante.objects.filter(slug__gte=slug)
        qs_json = serializers.serialize('json',qs)
        return Response(qs_json)