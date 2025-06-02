from django.db import models


class Pessoa(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    job = models.CharField(max_length=150)
    company = models.CharField(max_length=200)
    birthday = models.DateField()
    bank = models.CharField(max_length=200)
    credit_card = models.CharField(
        max_length=20
    )  # Número de cartão (precaução: criptografar em produção)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)  # CPF formatado (xxx.xxx.xxx-xx)
    cnpj = models.CharField(
        max_length=18, blank=True, null=True
    )  # CNPJ formatado (xx.xxx.xxx/xxxx-xx)
    rg = models.CharField(
        max_length=12, blank=True, null=True
    )  # RG pode variar por estado

    def __str__(self):
        return f"{self.name} - {self.cpf}"
