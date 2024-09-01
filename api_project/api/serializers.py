from rest_framework import serializers
from .models import BooK

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooK
        fields = '_all_'
    