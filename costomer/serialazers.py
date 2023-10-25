from rest_framework import serializers
from .models import Costomer, Shopcard
from shop.serialazer import Praductserializers

class Costomerserializers(serializers.ModelSerializer):
    class Meta:
        model = Costomer
        fields = ['id', 'name', 'location', 'email', 'number']

class UpdateCostomerserialazer(serializers.ModelSerializer):

    class Meta:
        model = Costomer
        fields = ['id', 'name', 'location', 'email', 'number']

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.location = validated_data.get("location", instance.location)
        instance.email = validated_data.get("email", instance.email)
        instance.number = validated_data.get("number", instance.number)

class Shopcardserializers(serializers.ModelSerializer):
    class Meta:
        model = Shopcard
        fields = ['id', 'date','praduct','owner','paymant']

class UpdateShopcardserialazer(serializers.ModelSerializer):

    class Meta:
        model = Shopcard
        fields = ['id', 'date','praduct','owner','paymant']

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.date = validated_data.get("date", instance.date)
        instance.praduct = validated_data.get("praduct", instance.praduct)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.paymant = validated_data.get("paymant", instance.paymant)

