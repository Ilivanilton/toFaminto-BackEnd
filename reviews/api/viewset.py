from django.shortcuts import render
from rest_framework import viewsets
from reviews.models import Review
from reviews.api.serializers import ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    filterset_fields = ['restaurantId']