from django.shortcuts import render
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class horaparqueoViewSet(viewsets.ModelViewSet):

    queryset = horaparqueo.objects.all()
    serializers_class = facturacionSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = ([JWTAuthentication])
# Create your views here.
