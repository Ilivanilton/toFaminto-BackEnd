from django.db import models

class Restaurante(models.Model):
    slug = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    deliveryEstimate = models.CharField(max_length=20)
    rating = models.DecimalField(decimal_places=2,max_digits=3)
    imagePath = models.CharField(max_length=200)
    about = models.TextField()
    hours = models.TextField()

    def __str__(self):
        return self.name


"""
  "restaurants": [
    {
      "id": "bread-bakery",
      "name": "Bread & Bakery",
      "category": "Bakery",
      "deliveryEstimate": "25m",
      "rating": 4.9,
      "imagePath": "assets/img/restaurants/breadbakery.png",
      "about": "A Bread & Brakery tem 40 anos de mercado. Fazemos os melhores doces e pães. Compre e confira.",
      "hours": "Funciona de segunda à sexta, de 8h às 23h"
    },
"""