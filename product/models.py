from django.db import models

CATEGORY_CHOICES = (
    ("Beds", "Beds"),
    ("Tables", "Tables"),
    ("Sofas", "Sofas"),
)


class Product(models.Model):
    thumbnail = models.ImageField(upload_to="product_thumbnails")

    cover = models.ImageField(upload_to="product_covers")

    sub_cover1 = models.ImageField(
        upload_to="cub_covers", blank=True, null=True)
    sub_cover2 = models.ImageField(
        upload_to="cub_covers", blank=True, null=True)
    sub_cover3 = models.ImageField(
        upload_to="cub_covers", blank=True, null=True)
    sub_cover4 = models.ImageField(
        upload_to="cub_covers", blank=True, null=True)

    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40, choices=CATEGORY_CHOICES)

    quality_one = models.CharField(
        max_length=100, default="", blank=True)
    quality_two = models.CharField(
        max_length=100, default="", blank=True)

    decription = models.TextField()

    price = models.DecimalField(decimal_places=2, max_digits=10000)

    width = models.IntegerField()
    height = models.IntegerField()
    length = models.IntegerField(blank=True, null=True)

    slug = models.SlugField(
        default="please-input-in-this-format", max_length=100)

    def __str__(self):
        return f"{self.name}, {self.category}"
