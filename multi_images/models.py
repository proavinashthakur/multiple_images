from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=120)
    descp = models.CharField(max_length=500)


class Images(models.Model):
    product = models.ForeignKey(null=False, related_name='images')
    images = models.ImageField(upload_to='products')
