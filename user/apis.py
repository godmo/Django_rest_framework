# from rest_framework import generics
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import Post
# from .serializers import PostSerializer

# @api_view
# def post_list(request):
#     posts = Post.objects.filter(status=Post.STATUS_NORMAL)
#     post_serializers = PostSerializer(posts,many=True)
#     return Response(post_serializers.data)
#     # url : http://127.0.0.1:8000/api/post/?format=json

# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.filter(status=Post.STATUS_NORMAL)
#     serializer_class = PostSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from .models import Music, Book
from .serializers import (
    MusicSerializer,
    MusicDetailSerializer,
    BookSerializer,
    BookDetailSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from django.http import JsonResponse


class MusicViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.filter()
    # permission_classes = [IsAdminUser]
    # def retrieve(self, request, *args, **kwargs):
    #     self.serializer_class = MusicDetailSerializer
    #     return super().retrieve(request, *args, **kwargs)

    # def filter_queryset(self, queryset):
    #     singer_id = self.request.query_params.get("singer")
    #     if singer_id:
    #         queryset = queryset.filter(singer=singer_id)
    #     return queryset

    @action(detail=False, methods=["get"])
    def test(self, request, pk=None):
        queryset = Music.objects.raw("SELECT * FROM music")
        serializer = MusicSerializer(queryset, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = MusicSerializer
    queryset = Music.objects.filter()
    # permission_classes = [IsAdminUser]
    # def retrieve(self, request, *args, **kwargs):
    #     self.serializer_class = MusicDetailSerializer
    #     return super().retrieve(request, *args, **kwargs)

    # def filter_queryset(self, queryset):
    #     singer_id = self.request.query_params.get("singer")
    #     if singer_id:
    #         queryset = queryset.filter(singer=singer_id)
    #     return queryset

    @action(detail=False, methods=["get"])
    def test(self, request, pk=None):
        queryset = Music.objects.raw("SELECT * FROM music")
        serializer = MusicSerializer(queryset, many=True)
        return Response(serializer.data)