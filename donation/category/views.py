from django.shortcuts import render


from rest_framework import generics
from category.serializers import CategorySerializer
from category.models import Category

from rest_framework.permissions import (
    IsAuthenticated,

    )

class CategoryList(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    	
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# Create your views here.
