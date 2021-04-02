from django.db import models


class Paciente(models.Model):
    paciente_id                = models.TextField(unique=True)
    paciente_sexo              = models.TextField()
    numero_acesso              = models.TextField()
    data_estudo                = models.TextField()
    espacamento_slice          = models.TextField()
    def __str__(self):
       return self.paciente_id
    class Meta:
        db_table = 'Paciente'
    

class Diagnostico(models.Model):
    paciente_id                = models.OneToOneField(Paciente, to_field='paciente_id', on_delete=models.CASCADE, unique=True)
    diagnostico                = models.CharField(max_length=11,choices=[('pneumonia','Pneumonia'),('tuberculose','Tuberculose'),('normal','Normal')])
    grau_de_severidade         = models.CharField(max_length=11,choices=[('grave','Grave'),('moderado','Moderado'),('leve','Leve'),('ausente','Ausente')])
    nivel_de_normalidade       = models.CharField(max_length = 10, choices=[('tipico','Típico'),('atipico','Atípico')])
    class Meta:
        db_table = 'Diagnóstico'




# Create your models here.
