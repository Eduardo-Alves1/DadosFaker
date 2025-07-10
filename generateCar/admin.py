from django.contrib import admin
from .models import Veiculo


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = [
        'placa', 'marca', 'modelo', 'ano_fabricacao', 
        'categoria', 'situacao', 'created_at'
    ]
    list_filter = [
        'categoria', 'especie', 'situacao', 'combustivel', 
        'cambio', 'ano_fabricacao', 'marca'
    ]
    search_fields = [
        'placa', 'chassi', 'renavan', 'marca', 'modelo', 
        'proprietario_nome', 'proprietario_cpf'
    ]
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('placa', 'chassi', 'renavan', 'situacao')
        }),
        ('Fabricante', {
            'fields': ('marca', 'modelo', 'ano_fabricacao', 'ano_modelo')
        }),
        ('Características Técnicas', {
            'fields': ('cor', 'combustivel', 'motor', 'potencia', 'cambio')
        }),
        ('Classificação', {
            'fields': ('categoria', 'especie', 'tipo')
        }),
        ('Especificações', {
            'fields': ('numero_portas', 'numero_passageiros', 'capacidade_carga')
        }),
        ('Documentação', {
            'fields': ('data_emissao', 'data_vencimento')
        }),
        ('Proprietário', {
            'fields': ('proprietario_nome', 'proprietario_cpf', 'proprietario_endereco')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    ordering = ['-created_at']
    list_per_page = 25
