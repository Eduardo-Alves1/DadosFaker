from django.db import models


class Veiculo(models.Model):
    # Informações básicas do veículo
    placa = models.CharField(max_length=8, unique=True)  # Formato: ABC-1234 ou ABC1D23
    chassi = models.CharField(max_length=17, unique=True)  # VIN padrão internacional
    renavan = models.CharField(max_length=11, unique=True)  # Código RENAVAM brasileiro
    
    # Informações do fabricante
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_fabricacao = models.IntegerField()
    ano_modelo = models.IntegerField()
    
    # Características técnicas
    cor = models.CharField(max_length=50)
    combustivel = models.CharField(max_length=30)
    motor = models.CharField(max_length=50)  # Ex: 1.0, 2.0 Turbo
    potencia = models.CharField(max_length=20)  # Ex: 100cv, 150hp
    cambio = models.CharField(max_length=20)  # Manual, Automático, CVT
    
    # Informações de documentação
    categoria = models.CharField(max_length=20)  # Passeio, Utilitário, Carga, etc.
    especie = models.CharField(max_length=20)  # Automóvel, Motocicleta, Caminhão, etc.
    tipo = models.CharField(max_length=30)  # Sedan, Hatch, SUV, etc.
    
    # Informações adicionais
    numero_portas = models.IntegerField()
    numero_passageiros = models.IntegerField()
    capacidade_carga = models.CharField(max_length=20, blank=True, null=True)
    
    # Datas importantes
    data_emissao = models.DateField()
    data_vencimento = models.DateField()
    
    # Informações do proprietário (simuladas)
    proprietario_nome = models.CharField(max_length=200)
    proprietario_cpf = models.CharField(max_length=14)
    proprietario_endereco = models.TextField()
    
    # Status do veículo
    situacao = models.CharField(max_length=20, default='Ativo')  # Ativo, Inativo, Roubado, etc.
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} - {self.placa}"

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['-created_at']
