from django.db import models


class Paciente(models.Model):
    paciente_id                = models.TextField(blank = True,unique=True, primary_key=True)
    paciente_sexo              = models.TextField(blank = True)
    numero_acesso              = models.TextField(blank = True)
    data_estudo                = models.TextField(blank = True)
    espacamento_slice          = models.TextField(blank = True)
    imagem                     = models.TextField()
    diagnostico                = models.CharField(blank = True, max_length=11,choices=[('pneumonia','Pneumonia'),('tuberculose','Tuberculose'),('normal','Normal')])
    grau_de_severidade         = models.CharField(blank = True,max_length=11,choices=[('grave','Grave'),('moderado','Moderado'),('leve','Leve'),('ausente','Ausente')])
    nivel_de_normalidade       = models.CharField(blank = True,max_length = 10, choices=[('tipico','Típico'),('atipico','Atípico')])
    def __str__(self):
       return self.paciente_id
    class Meta:
        db_table = 'Paciente'
    




# Create your models here.
