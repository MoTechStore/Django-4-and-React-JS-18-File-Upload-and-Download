from django.shortcuts import render
from .models import Files
from rest_framework import viewsets
from .serializers import FilesSerializer

# Create your views here.

class FilesViewSet(viewsets.ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
