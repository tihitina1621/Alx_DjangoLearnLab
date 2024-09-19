from rest_framework import serializers
from .models import Book, Author
from django.utils import timezone


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name'] 

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  #creates a nested representation of the author data iinside the book's data
    class Meta:
        model = Book
        fields = '_all_'
    
    def validate(self, data):
        current_time = timezone.now
        publication_year = data.get('publication_year')
        if publication_year > current_time:
            raise serializers.ValidationError("The publication year is not correct.")
        return data