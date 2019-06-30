from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerialiazer

class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerialiazer
# Create your views here.
