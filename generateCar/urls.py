from django.urls import path
from .views import (
    VeiculoGenerateAPIView,
    VeiculoListAPIView,
    VeiculoDetailAPIView,
    save_veiculo_to_db,
    veiculo_pronto,
    estatisticas_veiculos,
    limpar_veiculos
)

app_name = 'generateCar'

urlpatterns = [
    # Geração de veículos (sem salvar no banco)
    path('veiculos/generate/', VeiculoGenerateAPIView.as_view(), name='generate-veiculos'),
    path('veiculos/pronto/', veiculo_pronto, name='veiculo-pronto'),
    
    # Salvamento no banco de dados
    path('veiculos/save/', save_veiculo_to_db, name='save-veiculos'),
    
    # Consulta de veículos salvos
    path('veiculos/', VeiculoListAPIView.as_view(), name='list-veiculos'),
    path('veiculos/<int:id>/', VeiculoDetailAPIView.as_view(), name='detail-veiculo'),
    
    # Estatísticas e manutenção
    path('veiculos/stats/', estatisticas_veiculos, name='estatisticas-veiculos'),
    path('veiculos/limpar/', limpar_veiculos, name='limpar-veiculos'),
]
