from rest_framework import serializers
from .models import BooK

class BookSerializer(serializers.Modelserializer):
    class Meta:
        model = BooK
        fields = '_all_'
    