from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.


class BlogList(generics.ListAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blog.objects.all()
    serializer_class = BlogSerializer