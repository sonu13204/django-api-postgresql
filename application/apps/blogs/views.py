from django.contrib.auth.models import User
from .models import Blogs
from rest_framework import generics
from .serializers import BlogSerializer


class BlogView(generics.ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer


class BlogCreateView(generics.CreateAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer


class BlogUpdateView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

    def perform_update(self, serializer):
        serializer.save()


class DestroyView(generics.DestroyAPIView):
    #permission_classes = (IsAuthenticated,)
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializer

    def perform_delete(self, serializer):
        serializer.delete()