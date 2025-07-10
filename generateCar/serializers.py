from rest_framework import serializers
from .models import Veiculo


class VeiculoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Veiculo"""
    
    class Meta:
        model = Veiculo
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class VeiculoRequestSerializer(serializers.Serializer):
    """Serializer para requisições de geração de veículos"""
    quantity = serializers.IntegerField(
        min_value=1, 
        max_value=100, 
        default=1,
        help_text="Quantidade de veículos a serem gerados (máximo 100)"
    )
    tipo_veiculo = serializers.ChoiceField(
        choices=[
            ('carro', 'Carro'),
            ('moto', 'Moto'),
            ('caminhao', 'Caminhão'),
            ('todos', 'Todos os tipos')
        ],
        default='todos',
        required=False,
        help_text="Tipo específico de veículo a ser gerado"
    )
    formato_placa = serializers.ChoiceField(
        choices=[
            ('mercosul', 'Mercosul (ABC1D23)'),
            ('antiga', 'Antiga (ABC-1234)'),
            ('aleatoria', 'Aleatória')
        ],
        default='aleatoria',
        required=False,
        help_text="Formato da placa a ser gerada"
    )


class VeiculoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem de veículos"""
    
    class Meta:
        model = Veiculo
        fields = [
            'id', 'placa', 'marca', 'modelo', 'ano_fabricacao', 
            'cor', 'categoria', 'situacao', 'created_at'
        ] 