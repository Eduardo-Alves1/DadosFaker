# 🚗 API de Geração de Dados de Veículos Brasileiros

Este app gera dados falsos de veículos brasileiros, incluindo placas (formato antigo e Mercosul), chassi, RENAVAM e informações completas do veículo.

## 📋 Funcionalidades

### ✅ Dados Gerados
- **Placa**: Formato antigo (ABC-1234) ou Mercosul (ABC1D23)
- **Chassi**: VIN padrão internacional (17 caracteres)
- **RENAVAM**: Código brasileiro (11 dígitos)
- **Informações do veículo**: Marca, modelo, ano, cor, etc.
- **Dados do proprietário**: Nome, CPF, endereço
- **Documentação**: Datas de emissão e vencimento

### 🚙 Tipos de Veículos Suportados
- **Carros**: Sedan, Hatch, SUV, Coupé
- **Motos**: Motocicletas
- **Caminhões**: Veículos de carga
- **Utilitários**: Vans, Pickups

## 🔗 Endpoints da API

### 1. Gerar Veículos (sem salvar no banco)
```http
POST /api/veiculos/veiculos/generate/
```

**Parâmetros:**
```json
{
    "quantity": 5,
    "tipo_veiculo": "carro",
    "formato_placa": "mercosul"
}
```

**Resposta:**
```json
{
    "message": "5 veículo(s) gerado(s) com sucesso",
    "veiculos": [...]
}
```

### 2. Veículo Pronto (um só)
```http
GET /api/veiculos/veiculos/pronto/
```

### 3. Salvar Veículos no Banco
```http
POST /api/veiculos/veiculos/save/
```

**Parâmetros:** Mesmo formato do generate

### 4. Listar Veículos Salvos
```http
GET /api/veiculos/veiculos/
GET /api/veiculos/veiculos/?marca=Fiat&categoria=Passeio
```

### 5. Detalhes de um Veículo
```http
GET /api/veiculos/veiculos/{id}/
```

### 6. Estatísticas
```http
GET /api/veiculos/veiculos/stats/
```

### 7. Limpar Banco
```http
DELETE /api/veiculos/veiculos/limpar/
```

## 📊 Parâmetros Disponíveis

### Tipo de Veículo
- `carro` - Automóveis de passeio
- `moto` - Motocicletas
- `caminhao` - Veículos de carga
- `todos` - Todos os tipos (padrão)

### Formato de Placa
- `mercosul` - ABC1D23
- `antiga` - ABC-1234
- `aleatoria` - Formato aleatório (padrão)

### Filtros para Listagem
- `marca` - Filtrar por marca
- `categoria` - Filtrar por categoria
- `situacao` - Filtrar por situação

## 🎯 Exemplos de Uso

### Gerar 3 carros com placa Mercosul
```bash
curl -X POST http://localhost:8000/api/veiculos/veiculos/generate/ \
  -H "Content-Type: application/json" \
  -d '{"quantity": 3, "tipo_veiculo": "carro", "formato_placa": "mercosul"}'
```

### Gerar 1 moto
```bash
curl -X POST http://localhost:8000/api/veiculos/veiculos/generate/ \
  -H "Content-Type: application/json" \
  -d '{"quantity": 1, "tipo_veiculo": "moto"}'
```

### Listar veículos Fiat
```bash
curl http://localhost:8000/api/veiculos/veiculos/?marca=Fiat
```

## 📋 Estrutura dos Dados

### Exemplo de Veículo Gerado
```json
{
    "placa": "ABC1D23",
    "chassi": "1HGBH41JXMN109186",
    "renavan": "12345678901",
    "marca": "Fiat",
    "modelo": "Uno",
    "ano_fabricacao": 2020,
    "ano_modelo": 2021,
    "cor": "Branco",
    "combustivel": "Flex",
    "motor": "1.0",
    "potencia": "100cv",
    "cambio": "Manual",
    "categoria": "Passeio",
    "especie": "Automóvel",
    "tipo": "Hatch",
    "numero_portas": 4,
    "numero_passageiros": 5,
    "capacidade_carga": null,
    "data_emissao": "2020-03-15",
    "data_vencimento": "2025-03-15",
    "proprietario_nome": "João Silva",
    "proprietario_cpf": "123.456.789-00",
    "proprietario_endereco": "Rua das Flores, 123 - São Paulo/SP",
    "situacao": "Ativo"
}
```

## 🛠️ Configuração do Admin

O modelo está configurado no Django Admin com:
- Lista organizada por campos principais
- Filtros por categoria, marca, situação
- Busca por placa, chassi, proprietário
- Campos organizados em seções

## 🔧 Tecnologias Utilizadas

- **Django 5.2.1** - Framework web
- **Django REST Framework** - API REST
- **Faker** - Geração de dados falsos
- **SQLite** - Banco de dados

## 🚀 Como Executar

1. **Instalar dependências:**
```bash
pip install -r requirements.txt
```

2. **Executar migrações:**
```bash
python manage.py migrate
```

3. **Criar superusuário (opcional):**
```bash
python manage.py createsuperuser
```

4. **Executar servidor:**
```bash
python manage.py runserver
```

5. **Acessar:**
- API: http://localhost:8000/api/veiculos/veiculos/
- Admin: http://localhost:8000/admin/ 