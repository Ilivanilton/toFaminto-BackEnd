from rest_framework import serializers
from restaurantes.models import Restaurante


class RestauranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurante
        fields = ['id', 'slug', 'name', 'category',
        'deliveryEstimate', 'rating', 'imagePath',
        'about', 'hours']