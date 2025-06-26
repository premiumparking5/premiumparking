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

from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
class LoginViewSet(viewsets.ViewSet):
"""
ViewSet para autenticar usuarios vía GET.
Endpoint: /api/login/?username=<user>&password=<pass>
"""
serializer_class = LoginSerializer
def list(self, request):
serializer =
self.serializer_class(data=request.query_params)
serializer.is_valid(raise_exception=True)
user = authenticate(
username=serializer.validated_data['username'],
password=serializer.validated_data['password']
)
if user:
return Response({
'success': True,
'user_id': user.id,
'username': user.username
}, status=status.HTTP_200_OK)
return Response({
'success': False,
'error': 'Credenciales inválidas'
}, status=status.HTTP_401_UNAUTHORIZED)
