from rest_framework import serializers
from .models import Language

class LanguageSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id','name','paradigm')