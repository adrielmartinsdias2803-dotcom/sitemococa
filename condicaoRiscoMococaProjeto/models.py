from django.db import models
from django.contrib.auth.models import User

class Cargo(models.Model):
    nome = models.CharField(max_length=100, unique=True, verbose_name="Nome do Cargo")
    
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"

    def __str__(self):
        return self.nome
class FuncionarioProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    cargo = models.ForeignKey(
        Cargo, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Cargo na Empresa"
    )

    def __str__(self):
        cargo_nome = self.cargo.nome if self.cargo else "Sem Cargo"
        return f"{self.user.username} - {cargo_nome}"