from django.db import models
from apps.products.models import MeasureUnit,CategoryProduct,Indicator

from rest_framework import serializers

class MeasureUnitSerializer(serializers.serializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state',)

class CategoryProductSerializer(serializers.serializer):

    class Meta:
        model = CategoryProduct
        exclude = ('state',)

class IndicatorSerializer(serializers.serializer):

    class Meta:
        model = Indicator
        exclude = ('state',)