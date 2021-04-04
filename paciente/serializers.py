from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Paciente



class PacienteSerializer(ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('__all__')

