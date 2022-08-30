from rest_framework import serializers
from . import models


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Coin
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=False, read_only=True)
    coin = CoinSerializer(many=False, read_only=True)

    class Meta:
        model = models.Event
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = '__all__'
