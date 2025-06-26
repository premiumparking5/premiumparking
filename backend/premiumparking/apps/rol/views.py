from django.shortcuts import render
from rest_framework import viewsets
from .models import *

from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import *


class RolViewSet(viewsets.ModelViewSet):

    queryset = Rol.objects.all()
    serializers_class = RolSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = ([JWTAuthentication])
    


# Create your views here.
