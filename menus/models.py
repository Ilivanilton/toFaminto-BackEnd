from django.db import models
from restaurantes.models import Restaurante

class Menu(models.Model):
    slug = models.CharField(max_length=200)
    imagePath = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=3)
    restaurantId = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

"""
  "menu": [
    {
      "id": "cup-cake",
      "imagePath": "assets/img/foods/cupcake.png",
      "name": "Cup Cake",
      "description": "Cup Cake recheado de Doce de Leite",
      "price": 8.7,
      "restaurantId": "bread-bakery"
    },
"""