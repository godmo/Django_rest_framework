from rest_framework import serializers
from .models import Music, Book


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ["song", "singer"]


class MusicDetailSerializer(MusicSerializer):
    class Meta:
        model = Music
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["author", "title"]


class BookDetailSerializer(BookSerializer):
    class Meta:
        model = Book
        fields = ["author", "title", "created"]
