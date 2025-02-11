from django.db import models

class Estudante(models.Model):
    nome = models.CharField(max_length = 1000)
    email = models.EmailField(max_length = 30, blank=False)
    cpf = models.CharField(max_length = 11)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length = 14)

    def __str__(self):
        return self.nome      
    
class Curso(models.Model):
    NIVEL =(
        ('B', 'Básico'),
        ('I', 'Itermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length = 10)
    descricao = models.CharField(max_length = 100, blank=False)
    nivel = models.CharField(max_length = 1, choices = NIVEL,blank=False, null=False, default = 'B')

    def __str__(self):
        return self.codigo                      
