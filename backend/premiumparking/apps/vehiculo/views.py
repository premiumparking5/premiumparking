from django.shortcuts import render
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class vehiculosViewSet(viewsets.ModelViewSet):

    queryset = vehiculos.objects.all()
    serializers_class = vehiculosSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = ([JWTAuthentication])
# Create your views here.
