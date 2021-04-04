from django.urls import path
from rest_framework import routers
from .views import PacienteView
from .models import Paciente

router = routers.DefaultRouter()
router.register('paciente',PacienteView,basename='Paciente')


urlpatterns=router.urls

