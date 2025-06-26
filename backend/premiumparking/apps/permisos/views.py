from django.shortcuts import render
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class permisosViewSet(viewsets.ModelViewSet):

    queryset = permisos.objects.all()
    serializers_class = permisosSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = ([JWTAuthentication])
# Create your views here.
