from django.shortcuts import render
from rest_framework import generics
from . serialzers import BlogPostSerializer

from.models import BlogPost
# Create your views here.
class BlogPostCreate(generics.ListCreateAPIview):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostListCreate(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"