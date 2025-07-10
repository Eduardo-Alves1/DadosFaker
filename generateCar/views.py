from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.db.models import Count
from .models import Veiculo
from .serializers import (
    VeiculoSerializer, 
    VeiculoRequestSerializer, 
    VeiculoListSerializer
)
from .faker_generate_car import (
    generate_veiculo_data, 
    generate_multiple_veiculos, 
    generate_veiculo_by_type,
    gerar_placa_mercosul,
    gerar_placa_antiga
)
import random


def gerar_veiculos_util(quantity, tipo_veiculo, formato_placa):
    """Função utilitária para geração de veículos falsos"""
    if tipo_veiculo == 'todos':
        veiculos_data = generate_multiple_veiculos(quantity)
    else:
        veiculos_data = generate_veiculo_by_type(tipo_veiculo, quantity)

    # Aplica formato de placa específico se solicitado
    if formato_placa != 'aleatoria':
        for veiculo in veiculos_data:
            if formato_placa == 'mercosul':
                veiculo['placa'] = gerar_placa_mercosul()
            elif formato_placa == 'antiga':
                veiculo['placa'] = gerar_placa_antiga()
    return veiculos_data


def resposta_padrao(success, message, data=None, status_code=status.HTTP_200_OK):
    resp = {
        'success': success,
        'message': message
    }
    if data is not None:
        resp['data'] = data
    return Response(resp, status=status_code)


class VeiculoGenerateAPIView(generics.GenericAPIView):
    """API para gerar veículos falsos"""
    serializer_class = VeiculoRequestSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        quantity = serializer.validated_data.get('quantity', 1)
        tipo_veiculo = serializer.validated_data.get('tipo_veiculo', 'todos')
        formato_placa = serializer.validated_data.get('formato_placa', 'aleatoria')

        veiculos_data = gerar_veiculos_util(quantity, tipo_veiculo, formato_placa)

        return resposta_padrao(
            True,
            f'{quantity} veículo(s) gerado(s) com sucesso',
            data=veiculos_data
        )


class VeiculoListAPIView(generics.ListAPIView):
    """API para listar veículos salvos no banco"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoListSerializer
    
    def get_queryset(self):
        queryset = Veiculo.objects.all()
        
        # Filtros opcionais
        marca = self.request.query_params.get('marca', None)
        categoria = self.request.query_params.get('categoria', None)
        situacao = self.request.query_params.get('situacao', None)
        
        if marca:
            queryset = queryset.filter(marca__icontains=marca)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if situacao:
            queryset = queryset.filter(situacao=situacao)
            
        return queryset


class VeiculoDetailAPIView(generics.RetrieveAPIView):
    """API para detalhes de um veículo específico"""
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    lookup_field = 'id'


@api_view(['POST'])
def save_veiculo_to_db(request):
    """Salva um veículo gerado no banco de dados"""
    serializer = VeiculoRequestSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    quantity = serializer.validated_data.get('quantity', 1)
    tipo_veiculo = serializer.validated_data.get('tipo_veiculo', 'todos')
    formato_placa = serializer.validated_data.get('formato_placa', 'aleatoria')

    veiculos_data = gerar_veiculos_util(quantity, tipo_veiculo, formato_placa)

    veiculos_salvos = []
    erros = []
    for veiculo_data in veiculos_data:
        try:
            veiculo = Veiculo.objects.create(**veiculo_data)
            veiculos_salvos.append(VeiculoSerializer(veiculo).data)
        except Exception as e:
            erros.append({'dados': veiculo_data, 'erro': str(e)})

    if erros:
        return resposta_padrao(
            False,
            f'{len(erros)} veículo(s) não foram salvos devido a erro. Veja detalhes em data.erros.',
            data={'veiculos_salvos': veiculos_salvos, 'erros': erros},
            status_code=status.HTTP_400_BAD_REQUEST
        )
    else:
        return resposta_padrao(
            True,
            f'{quantity} veículo(s) salvo(s) no banco com sucesso',
            data=veiculos_salvos,
            status_code=status.HTTP_201_CREATED
        )


@api_view(['GET'])
def veiculo_pronto(request):
    """Retorna um veículo pronto sem salvar no banco"""
    veiculo_data = generate_veiculo_data()
    return resposta_padrao(True, 'Veículo gerado com sucesso', data=veiculo_data)


@api_view(['GET'])
def estatisticas_veiculos(request):
    """Retorna estatísticas dos veículos no banco (otimizado)"""
    total_veiculos = Veiculo.objects.count()
    stats_categoria = {c['categoria']: c['total'] for c in Veiculo.objects.values('categoria').annotate(total=Count('id'))}
    stats_marca = {m['marca']: m['total'] for m in Veiculo.objects.values('marca').annotate(total=Count('id'))}
    stats_situacao = {s['situacao']: s['total'] for s in Veiculo.objects.values('situacao').annotate(total=Count('id'))}

    return resposta_padrao(
        True,
        'Estatísticas obtidas com sucesso',
        data={
            'total_veiculos': total_veiculos,
            'por_categoria': stats_categoria,
            'por_marca': stats_marca,
            'por_situacao': stats_situacao
        }
    )


@api_view(['DELETE'])
def limpar_veiculos(request):
    """Remove todos os veículos do banco de dados"""
    count = Veiculo.objects.count()
    Veiculo.objects.all().delete()
    return resposta_padrao(True, f'{count} veículo(s) removido(s) do banco com sucesso')
