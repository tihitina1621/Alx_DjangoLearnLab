from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']
    def validation(seld, date):
        date = 'publication_year'
        current_time = datetime.now()
        if date < current_time:
            raise serializers.ValidationError('The publication year is incorrect.')
        return date
class AuthorSerializer(serializers.ModelSerializer):
    dynamic = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'name', 'dynamic']
