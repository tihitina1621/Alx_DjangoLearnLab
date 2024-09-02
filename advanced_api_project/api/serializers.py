from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        filds = '_all_'
    def validate(self, data):
        current_time = timezone.now()
        if data >= current_time:
            raise serializers.validationError('The publication year is not correst.')

#the serializer will maily do help in APis and data execahnge. we can also validate the data coming as it to meet our expectation.