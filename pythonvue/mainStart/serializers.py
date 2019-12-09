from rest_framework import serializers
from .models import mainStart
class mainStartSerializer(serializers.ModelSerializer):
    class Meta:
        model = mainStart
        fields = '__all__'