from django.shortcuts import render
from rest_framework import viewsets
from .models import TestData
from .serializers import TestDataSerializer

class TestDataViewSet(viewsets.ModelViewSet):
    """
    テスト用クエリビュー
    """
    queryset = TestData.objects.all()
    serializer_class = TestDataSerializer
