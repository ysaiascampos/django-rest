from django.db import models
from apps.products.models import Product

from rest_framework import serializers

class ProductSerializer(serializers.serializer):

    class Meta:
        model = Product
        exclude = ('state',)