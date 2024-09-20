from rest_framework import serializers
from .models import Posts, Comments

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '_all_'
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '_all_'

