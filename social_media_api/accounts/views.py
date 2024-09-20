from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
class ULV(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def     
    return Response
