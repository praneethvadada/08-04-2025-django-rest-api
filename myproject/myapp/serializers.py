# myapp/serializers.py
from rest_framework import serializers
from myapp.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    author = serializers.CharField()
    pages = serializers.IntegerField()

    def create(self, validated_data):
        return Book(**validated_data).save()

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
