from rest_framework import serializers
from .models import Rubiks

class RubiksSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    layers = serializers.IntegerField()
    brand = serializers.CharField(max_length=100)

    class Meta:
        model = Rubiks
        fields = ('__all__')

