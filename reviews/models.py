from django.db import models
from restaurantes.models import Restaurante

class Review(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateTimeField()
    rating = models.DecimalField(decimal_places=2,max_digits=3)
    comments = models.TextField()
    restaurantId = models.ForeignKey(Restaurante, on_delete=models.CASCADE)




'''

  "reviews": [
    {
      "name": "Julia",
      "date": "2017-01-23T18:25:43",
      "rating": 4.5,
      "comments": "Tudo muito bom, entrega no tempo certo",
      "restaurantId": "bread-bakery"
    },
'''