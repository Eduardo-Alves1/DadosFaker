import requests

from faker import Faker
import random
from datetime import datetime, timedelta

faker = Faker("pt_BR")


# Dados de marcas e modelos brasileiros
MARCAS_MODELOS = {
    "Fiat": ["Uno", "Palio", "Siena", "Strada", "Toro", "Argo", "Cronos", "Fastback"],
    "Volkswagen": ["Gol", "Voyage", "Saveiro", "Fox", "Polo", "Virtus", "T-Cross", "Nivus"],
    "Chevrolet": ["Onix", "Prisma", "Cobalt", "Spin", "Tracker", "Cruze", "Cobalt"],
    "Ford": ["Ka", "Fiesta", "Focus", "EcoSport", "Ranger", "Territory"],
    "Honda": ["Civic", "City", "Fit", "HR-V", "CR-V", "WR-V"],
    "Toyota": ["Corolla", "Etios", "Yaris", "SW4", "Hilux", "RAV4"],
    "Hyundai": ["HB20", "HB20S", "i30", "Tucson", "Santa Fe", "Creta"],
    "Renault": ["Kwid", "Sandero", "Logan", "Duster", "Captur", "Koleos"],
    "Nissan": ["March", "Versa", "Kicks", "Sentra", "X-Trail"],
    "Jeep": ["Renegade", "Compass", "Cherokee", "Gladiator"],
    "Mercedes-Benz": ["Classe A", "Classe C", "Classe E", "GLA", "GLC"],
    "BMW": ["Série 1", "Série 3", "Série 5", "X1", "X3", "X5"],
    "Audi": ["A3", "A4", "A6", "Q3", "Q5", "Q7"],
    "Peugeot": ["208", "2008", "3008", "408", "508"],
    "Citroën": ["C3", "C4", "C4 Cactus", "C5"],
}

CORES = [
    "Branco", "Preto", "Prata", "Cinza", "Azul", "Vermelho", 
    "Verde", "Amarelo", "Laranja", "Marrom", "Bege", "Dourado"
]

COMBUSTIVEIS = ["Gasolina", "Etanol", "Flex", "Diesel", "Elétrico", "Híbrido"]

CAMBIO = ["Manual", "Automático", "CVT", "Automatizado"]

CATEGORIAS = ["Passeio", "Utilitário", "Carga", "Transporte Coletivo"]

ESPECIES = ["Automóvel", "Motocicleta", "Caminhão", "Ônibus", "Utilitário"]

TIPOS = ["Sedan", "Hatch", "SUV", "Pickup", "Van", "Wagon", "Coupé", "Conversível"]

SITUACOES = ["Ativo", "Inativo", "Roubado", "Apreendido", "Destruído"]


def gerar_placa_mercosul():
    """Gera uma placa no padrão Mercosul (ABC1D23)"""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    
    # Formato: ABC1D23
    placa = ""
    placa += random.choice(letras)  # A
    placa += random.choice(letras)  # B
    placa += random.choice(letras)  # C
    placa += random.choice(numeros)  # 1
    placa += random.choice(letras)  # D
    placa += random.choice(numeros)  # 2
    placa += random.choice(numeros)  # 3
    
    return placa


def gerar_placa_antiga():
    """Gera uma placa no formato antigo (ABC-1234)"""
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    
    # Formato: ABC-1234
    placa = ""
    placa += random.choice(letras)  # A
    placa += random.choice(letras)  # B
    placa += random.choice(letras)  # C
    placa += "-"
    placa += random.choice(numeros)  # 1
    placa += random.choice(numeros)  # 2
    placa += random.choice(numeros)  # 3
    placa += random.choice(numeros)  # 4
    
    return placa


def gerar_chassi():
    """Gera um número de chassi (VIN) válido"""
    # VIN tem 17 caracteres: 3 dígitos do fabricante + 6 dígitos do modelo + 8 dígitos sequenciais
    caracteres = "0123456789ABCDEFGHJKLMNPRSTUVWXYZ"  # Sem I, O, Q
    
    chassi = ""
    for _ in range(17):
        chassi += random.choice(caracteres)
    
    return chassi


def gerar_renavan():
    """Gera um código RENAVAM válido (11 dígitos)"""
    # RENAVAM tem 11 dígitos
    renavan = ""
    for _ in range(11):
        renavan += str(random.randint(0, 9))
    
    return renavan


def gerar_motor():
    """Gera uma descrição de motor realista"""
    cilindradas = ["1.0", "1.2", "1.4", "1.6", "1.8", "2.0", "2.5", "3.0", "4.0"]
    tecnologias = ["", " Turbo", " TSI", " TDI", " GTI", " VVT"]
    
    motor = random.choice(cilindradas) + random.choice(tecnologias)
    return motor


def gerar_potencia():
    """Gera uma potência realista"""
    potencias = ["70cv", "80cv", "90cv", "100cv", "110cv", "120cv", "130cv", "140cv", "150cv", "170cv", "200cv", "250cv", "300cv"]
    return random.choice(potencias)


def gerar_capacidade_carga():
    """Gera capacidade de carga para veículos comerciais"""
    capacidades = ["500kg", "1000kg", "1500kg", "2000kg", "3000kg", "5000kg", "10000kg"]
    return random.choice(capacidades)


def generate_veiculo_data():
    """Gera dados completos de um veículo brasileiro"""
    # Escolhe formato de placa (antigo ou Mercosul)
    if random.choice([True, False]):
        placa = gerar_placa_mercosul()
    else:
        placa = gerar_placa_antiga()
    
    # Escolhe marca e modelo
    marca = random.choice(list(MARCAS_MODELOS.keys()))
    modelo = random.choice(MARCAS_MODELOS[marca])
    
    # Gera anos
    ano_atual = datetime.now().year
    ano_fabricacao = random.randint(2010, ano_atual)
    ano_modelo = ano_fabricacao + random.randint(0, 1)
    
    # Gera datas de documentação
    data_emissao = faker.date_between(start_date=f'-{ano_atual - ano_fabricacao}y', end_date='today')
    data_vencimento = data_emissao + timedelta(days=365 * 5)  # 5 anos
    
    # Determina tipo de veículo baseado na categoria
    categoria = random.choice(CATEGORIAS)
    if categoria == "Passeio":
        especie = "Automóvel"
        tipo = random.choice(["Sedan", "Hatch", "SUV", "Coupé"])
        numero_portas = random.choice([2, 4, 5])
        numero_passageiros = random.choice([2, 4, 5, 7])
        capacidade_carga = None
    elif categoria == "Utilitário":
        especie = "Utilitário"
        tipo = random.choice(["Van", "Pickup", "Wagon"])
        numero_portas = random.choice([2, 4, 5])
        numero_passageiros = random.choice([2, 4, 5, 8])
        capacidade_carga = gerar_capacidade_carga()
    else:  # Carga
        especie = "Caminhão"
        tipo = "Caminhão"
        numero_portas = 2
        numero_passageiros = 2
        capacidade_carga = gerar_capacidade_carga()
    
    return {
        "placa": placa,
        "chassi": gerar_chassi(),
        "renavan": gerar_renavan(),
        "marca": marca,
        "modelo": modelo,
        "ano_fabricacao": ano_fabricacao,
        "ano_modelo": ano_modelo,
        "cor": random.choice(CORES),
        "combustivel": random.choice(COMBUSTIVEIS),
        "motor": gerar_motor(),
        "potencia": gerar_potencia(),
        "cambio": random.choice(CAMBIO),
        "categoria": categoria,
        "especie": especie,
        "tipo": tipo,
        "numero_portas": numero_portas,
        "numero_passageiros": numero_passageiros,
        "capacidade_carga": capacidade_carga,
        "data_emissao": data_emissao.strftime("%Y-%m-%d"),
        "data_vencimento": data_vencimento.strftime("%Y-%m-%d"),
        "proprietario_nome": faker.name(),
        "proprietario_cpf": faker.cpf(),
        "proprietario_endereco": faker.address(),
        "situacao": random.choice(SITUACOES),
    }


def generate_multiple_veiculos(quantity=1):
    """Gera múltiplos veículos"""
    veiculos = []
    for _ in range(quantity):
        veiculos.append(generate_veiculo_data())
    return veiculos


def generate_veiculo_by_type(tipo_veiculo, quantity=1):
    """Gera veículos de um tipo específico"""
    veiculos = []
    
    for _ in range(quantity):
        veiculo = generate_veiculo_data()
        
        if tipo_veiculo.lower() == "carro":
            veiculo["categoria"] = "Passeio"
            veiculo["especie"] = "Automóvel"
            veiculo["tipo"] = random.choice(["Sedan", "Hatch", "SUV"])
        elif tipo_veiculo.lower() == "moto":
            veiculo["categoria"] = "Passeio"
            veiculo["especie"] = "Motocicleta"
            veiculo["tipo"] = "Motocicleta"
            veiculo["numero_portas"] = 0
            veiculo["numero_passageiros"] = 2
        elif tipo_veiculo.lower() == "caminhao":
            veiculo["categoria"] = "Carga"
            veiculo["especie"] = "Caminhão"
            veiculo["tipo"] = "Caminhão"
            veiculo["numero_portas"] = 2
            veiculo["numero_passageiros"] = 2
            veiculo["capacidade_carga"] = gerar_capacidade_carga()
        
        veiculos.append(veiculo)
    
    return veiculos
