from django.db import models
from product.models import Product


class Testimonial(models.Model):
    message = models.CharField(max_length=250)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PopularProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name="popular_product")

    def __str__(self):
        return self.product.name
