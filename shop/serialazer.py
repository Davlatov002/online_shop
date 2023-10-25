from rest_framework import serializers
from .models import Category, Praduct

class Categoriyserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class UpdateCategoriyserialazer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)


class Praductserializers(serializers.ModelSerializer):
    class Meta:
        model = Praduct
        fields = ('id', 'name','image','category_id','price','start_data','end_data')

class UpdatePraductserialazer(serializers.ModelSerializer):

    class Meta:
        model = Praduct
        fields = ['id', 'name','image','category_id','price','start_data','end_data']

    def update(self, instance, validated_data):
        instance.id = validated_data.get("id", instance.id)
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.category_id = validated_data.get("category_id", instance.category_id)
        instance.price = validated_data.get("price", instance.price)
        instance.start_data = validated_data.get("start_data", instance.start_data)
        instance.end_data = validated_data.get("end_data", instance.end_data)