from rest_framework import serializers
from .models import Shortened, ShortenRequest


class ShortenedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortened
        fields = ["id", "url", "shortCode", "createdAt", "updatedAt"]


class ShortenRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortenRequest
        fields = ["url"]
