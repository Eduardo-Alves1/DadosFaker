from faker import Faker


faker = Faker("pt_BR")


def generate_fake_data(fields: list, quantity: int = 1):
    data = []
    for _ in range(quantity):
        item = {}
        for field in fields:
            if hasattr(faker, field):
                item[field] = getattr(faker, field)()
            else:
                item[field] = f"Campo inválido: {field}"
        data.append(item)
    return data


def generate_fake_profile():
    nome = (
        faker.name()
        .replace("Dr.", "")
        .replace("Dra.", "")
        .replace("Sr.", "")
        .replace("Sra.", "")
        .strip()
    )
    nome_email = nome.lower().replace(" ", ".").replace("ç", "c").replace("é", "e")
    return {
        "nome": nome,
        "email": f"{nome_email}@egmail.com",
        "emailE2e": f"{nome_email}@e2etreinamentos.com.br",
        "cpf": faker.cpf().replace(".", "").replace("-", ""),
        "rg": faker.rg(),
        "celualar": faker.cellphone_number(),
        "endereco": faker.address(),
        "cep": faker.postcode(),
        "cidade": faker.city(),
        "estado": faker.state(),
        "pais": faker.country(),
        "data_nascimento": faker.date_of_birth(minimum_age=18, maximum_age=80).strftime(
            "%Y-%m-%d"
        ),
        "genero": faker.random_element(elements=("Masculino", "Feminino", "Outro")),
    }
