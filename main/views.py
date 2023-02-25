from rest_framework import generics, pagination
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Comment
from .serializers import (
    CommentListSerializer, 
    CommentDetailSerializer, 
    CommentCreateSerializer, 
    CommentUpdateSerializer, 
    CommentDeleteSerializer,
    CommentImageSerializer,
)

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.order_by('-id')
    serializer_class = CommentListSerializer
    pagination_class = CustomPagination

class CommentDetailView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDeleteSerializer


class CommentImageView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentImageSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = self.get_serializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        return self.put(request, *args, **kwargs)
