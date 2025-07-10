# DadosFaker

Repositório para geração e manipulação de dados fictícios, com foco em dados de veículos brasileiros, utilizando Django, Django REST Framework, Faker e frontend em React+Vite.

---

## 📁 Estrutura de Pastas

```
DadosFaker/
│
├── generateCar/           # Módulo Django para geração de veículos
│   └── README.md          # Documentação detalhada da API de veículos
├── frontend/              # Aplicação frontend em React + Vite
│   └── README.md
├── requirements.txt       # Dependências do backend Python/Django
├── manage.py              # Entrypoint do projeto Django
├── ...                    # Outros arquivos e módulos do Django
```

---

## ⚙️ Instalação e Execução

### 1. Clone o repositório

```bash
git clone https://github.com/Eduardo-Alves1/DadosFaker.git
cd DadosFaker
```

### 2. Instale as dependências do backend

```bash
pip install -r requirements.txt
```

### 3. Execute as migrações do banco de dados

```bash
python manage.py migrate
```

### 4. (Opcional) Crie um superusuário para o admin

```bash
python manage.py createsuperuser
```

### 5. Inicie o servidor Django

```bash
python manage.py runserver
```

### 6. (Opcional) Instale e rode o frontend

Veja instruções específicas no `frontend/README.md`.

---

## 🚗 API de Geração de Veículos

Documentação detalhada disponível em [`generateCar/README.md`](generateCar/README.md).

**Principais endpoints:**
- `POST /api/veiculos/veiculos/generate/` - Gera veículos fake (parâmetros: quantidade, tipo, formato placa)
- `GET /api/veiculos/veiculos/pronto/` - Retorna um veículo pronto
- `POST /api/veiculos/veiculos/save/` - Salva veículos gerados no banco
- `GET /api/veiculos/veiculos/` - Lista veículos salvos (com filtros: marca, categoria, situação)
- `GET /api/veiculos/veiculos/{id}/` - Detalhes de um veículo
- `GET /api/veiculos/veiculos/stats/` - Estatísticas
- `DELETE /api/veiculos/veiculos/limpar/` - Limpa o banco de veículos

**Exemplo de chamada com `curl`:**

```bash
curl -X POST http://localhost:8000/api/veiculos/veiculos/generate/ \
  -H "Content-Type: application/json" \
  -d '{"quantity": 3, "tipo_veiculo": "carro", "formato_placa": "mercosul"}'
```

**Exemplo de dado gerado:**

```json
{
  "placa": "ABC1D23",
  "chassi": "1HGBH41JXMN109186",
  "renavan": "12345678901",
  "marca": "Fiat",
  ...
}
```

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Django 5.2.1, Django REST Framework
- **Geração de dados:** Faker
- **Banco de dados:** SQLite (padrão Django)
- **Frontend:** React + Vite

---

## 📦 Dependências Python Principais (`requirements.txt`)

- Django==5.2.1
- djangorestframework==3.16.0
- Faker==37.3.0
- requests, asgiref, sqlparse, etc.

---

## 👨‍💻 Contribuição

Contribuições são bem-vindas! Abra issues ou pull requests.

---

## 📄 Licença

Este projeto não possui licença definida no momento.

---

## 👤 Autor

- Eduardo Alves — [GitHub](https://github.com/Eduardo-Alves1)

---

> Consulte as documentações em `generateCar/README.md` e `frontend/README.md` para instruções detalhadas de cada módulo.
