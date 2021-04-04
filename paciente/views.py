from django.shortcuts import render
from django.contrib.auth import get_user_model
from .models import Paciente
from rest_framework.viewsets import ModelViewSet
from .serializers import  PacienteSerializer



class PacienteView(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

