from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.models import Token

serializers.CharField()
Token.objects.create  get_user_model().objects.create_user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '_all_'