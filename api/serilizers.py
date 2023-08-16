from rest_framework import serializers
from .models import Data


#serilizer for Data model
class Dataserializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    #code for create object of data
    def create(self, validate_data):
        return Data.objects.create(**validate_data)
    #code for update objects(PUT & PATCH) of data
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.save()
        return instance
        

